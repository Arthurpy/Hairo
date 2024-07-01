<template>
  <div class="bg-blue-200 flex min-h-screen">
    <sidebar :activeButton="'notes'"/>
    <div class="flex flex-col ml-80 flex-grow items-center p-8">
      <div class="flex bg-white text-blue-600 w-full max-w-4xl rounded-lg justify-between items-center mt-10 py-4 px-8 shadow-md">
        <h1 class="search-title text-blue-600 text-4xl font-bold">Mes notes</h1>
      </div>
      <div class="main-content w-full flex flex-col items-center mt-8">
        <div class="mb-4 flex space-x-4" style="width: 60%; justify-content: space-around;">
          <button @click="handleAddButtonClick" style="font-size: larger" class="my-button">Ajouter</button>
          <button @click="handleDeleteButtonClick" style="font-size: larger" class="my-button">Supprimer</button>
        </div>
        <div class="note-container w-full flex flex-wrap justify-start">
          <template v-if="!selectedNotebook">
            <div v-for="notebook in notebooks" :key="notebook.id" class="note-card">
              <h2 class="note-title" @click="selectNotebook(notebook)">{{ notebook.displayName }}</h2>
            </div>
            <div v-for="i in placeholders(notebooks.length)" :key="'notebook-placeholder-' + i" class="note-card placeholder"></div>
          </template>
          <template v-else-if="selectedNotebook && !selectedSection">
            <div v-for="section in sections[selectedNotebook.id]" :key="section.id" class="note-card">
              <h2 class="note-title" @click="selectSection(section)">{{ section.displayName }}</h2>
            </div>
            <div v-for="i in placeholders(sections[selectedNotebook.id].length)" :key="'section-placeholder-' + i" class="note-card placeholder"></div>
          </template>
          <template v-else-if="selectedSection && !selectedNote">
            <div v-for="note in notes" :key="note.id" class="note-card">
              <h2 class="note-title" @click="selectNote(note)">{{ note.title }}</h2>
            </div>
            <div v-for="i in placeholders(notes.length)" :key="'note-placeholder-' + i" class="note-card placeholder"></div>
          </template>
          <template v-else>
            <div class="note-detail w-full flex flex-col items-center">
              <div class="note-card w-full max-w-4xl">
                <div class="flex flex-col">
                  <h2 class="note-title">{{ selectedNote.title }}</h2>
                  <div class="note-content" v-html="noteContent"></div>
                </div>
              </div>
              <div class="flex mt-4 space-x-4">
                <button @click="openEditNoteModal" class="my-button">Modifier</button>
                <button @click="deselectNote" class="my-button">Retour aux pages</button>
              </div>
              <div v-if="isEditNoteModalOpen" class="edit-note-modal">
                <div class="modal-content">
                  <h2>Editeur de texte</h2>
                  <quill-editor
                    v-model="editNoteInput"
                    :options="editorOptions"
                    class="editor"
                  ></quill-editor>
                  <div class="flex space-x-4 mt-4">
                    <button @click="saveNoteChanges" class="my-button">Sauvegarder</button>
                    <button @click="closeEditNoteModal" class="my-button">Annuler</button>
                  </div>
                </div>
              </div>
            </div>
          </template>
          <template v-if="selectedNotebook || selectedSection || selectedNote">
            <div class="mt-4 flex space-x-4">
              <button @click="deselectNotebook" class="my-button">Retour aux notebooks</button>
              <button @click="deselectSection" class="my-button">Retour à la section</button>
            </div>
          </template>
        </div>
      </div>
    </div>
    <Modal v-if="showModal" :title="modalTitle" :actionText="modalActionText" @close="closeModal" @submit="handleModalSubmit">
      <input v-model="modalInput" type="text" placeholder="Entrez le nom" class="input" style="background-color: white; color: black !important; border-radius: 10px;">
    </Modal>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import { reactive } from 'vue';
import { QuillEditor } from '@vueup/vue-quill';
import Modal from '../components/Modal.vue';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

export default {
  name: 'notes',
  components: {
    sidebar,
    Modal,
    QuillEditor
  },
  data() {
    return {
      accessToken: null,
      notebooks: [],
      pages: [],
      sections: reactive({}),
      selectedNotebook: null,
      selectedSection: null,
      notes: [],
      selectedNote: null,
      noteContent: '',
      isEditNoteModalOpen: false,
      editNoteTitle: '',
      editNoteContent: '',
      noteToEdit: null,
      editNoteInput: '',
      selectedItemId: [],
      showModal: false,
      modalTitle: '',
      modalActionText: '',
      modalInput: '',
      addType: null,
      editorOptions: {
        theme: 'snow',
        modules: {
          toolbar: [
            [{ 'header': [1, 2, false] }],
            ['bold', 'italic', 'underline'],
            [{ 'list': 'ordered'}, { 'list': 'bullet' }],
            ['link', 'image']
          ]
        }
      }
    };
  },
  methods: {
    openMicrosoftLogin() {
      window.location.href = 'http://localhost:8000/notes-login/';
    },
    async fetchNotebooks() {
      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        const url = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks';
        const response = await fetch(url, { headers });
        if (response.status === 401 || response.status === 403) {
          localStorage.removeItem('microsoft_access_token');
          this.accessToken = null;
          this.openMicrosoftLogin();
          return;
        }
        if (!response.ok) {
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        this.notebooks = data.value;
      } catch (error) {
        console.error('Error fetching notebooks:', error);
      }
    },
    async fetchSections(notebookId) {
      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        let url = `https://graph.microsoft.com/v1.0/me/onenote/notebooks/${notebookId}/sections`;
        let allSections = [];

        while (url) {
          const response = await fetch(url, { headers });
          if (!response.ok) {
            throw new Error(`API request failed: ${response.status} ${response.statusText}`);
          }
          const data = await response.json();
          allSections = allSections.concat(data.value);
          url = data['@odata.nextLink'];
        }

        this.sections[notebookId] = allSections;
      } catch (error) {
        console.error('Error fetching sections:', error);
      }
    },
    async fetchPages(sectionId) {
      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        let url = `https://graph.microsoft.com/v1.0/me/onenote/sections/${sectionId}/pages`;
        let allPages = [];

        while (url) {
          const response = await fetch(url, { headers });
          if (!response.ok) {
            throw new Error(`API request failed: ${response.status} ${response.statusText}`);
          }
          const data = await response.json();
          allPages = allPages.concat(data.value);
          url = data['@odata.nextLink'];
        }

        this.notes = allPages.map(page => ({
          id: page.id,
          title: page.title,
          contentUrl: page.contentUrl
        }));
      } catch (error) {
        console.error('Error fetching pages:', error);
      }
    },
    selectNotebook(notebook) {
      this.selectedNotebook = notebook;
      this.selectedSection = null;
      this.selectedNote = null;
      this.fetchSections(notebook.id);
    },
    selectSection(section) {
      this.selectedSection = section;
      this.selectedNote = null;
      this.fetchPages(section.id);
    },
    selectNote(note) {
      this.selectedNote = note;
      this.fetchNoteContent(note.contentUrl);
    },
    deselectNotebook() {
      this.selectedNotebook = null;
      this.selectedSection = null;
      this.selectedNote = null;
    },
    deselectSection() {
      this.selectedSection = null;
      this.selectedNote = null;
    },
    deselectNote() {
      this.selectedNote = null;
    },
    async fetchNoteContent(contentUrl) {
      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/xhtml+xml'
        });
        const response = await fetch(contentUrl, { headers });
        if (!response.ok) {
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        const content = await response.text();
        this.noteContent = content;
        return content;
      } catch (error) {
        console.error('Error fetching note content:', error);
        this.noteContent = '';
        return '';
      }
    },
    handleAddButtonClick() {
      if (this.selectedNotebook && !this.selectedSection) {
        this.modalTitle = 'Ajouter une nouvelle section';
        this.modalActionText = 'Ajouter';
        this.addType = 'section';
      } else if (this.selectedSection && !this.selectedNote) {
        this.modalTitle = 'Ajouter une nouvelle page';
        this.modalActionText = 'Ajouter';
        this.addType = 'page';
      } else if (!this.selectedNotebook) {
        this.modalTitle = 'Ajouter un nouveau notebook';
        this.modalActionText = 'Ajouter';
        this.addType = 'notebook';
      }
      this.showModal = true;
    },
    async createSection() {
      if (!this.modalInput) return;

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        const body = JSON.stringify({
          'displayName': this.modalInput
        });
        const url = `https://graph.microsoft.com/v1.0/me/onenote/notebooks/${this.selectedNotebook.id}/sections`;
        const response = await fetch(url, { method: 'POST', headers, body });
        if (!response.ok) {
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        this.fetchSections(this.selectedNotebook.id);
      } catch (error) {
        console.error('Error creating section:', error);
      }
    },
    async createPage() {
      if (!this.modalInput) return;

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/xhtml+xml'
        });
        const url = `https://graph.microsoft.com/v1.0/me/onenote/sections/${this.selectedSection.id}/pages`;
        const body = `
          <!DOCTYPE html>
          <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
              <title>${this.modalInput}</title>
            </head>
            <body>
            </body>
          </html>
        `;

        const response = await fetch(url, { method: 'POST', headers, body });
        if (!response.ok) {
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        const newPage = await response.json();
        this.notes.push({ id: newPage.id, title: newPage.title, contentUrl: newPage.contentUrl });
      } catch (error) {
        console.error('Error creating page:', error);
      }
    },
    async createNotebook() {
      if (!this.modalInput) return;

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        const url = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks';
        const body = JSON.stringify({
          'displayName': this.modalInput
        });
        const response = await fetch(url, { method: 'POST', headers, body });
        if (!response.ok) {
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        const newNotebook = await response.json();
        this.notebooks.push(newNotebook);
      } catch (error) {
        console.error('Error creating notebook:', error);
      }
    },
    handleModalSubmit() {
      this.showModal = false;
      if (this.addType === 'notebook') {
        this.createNotebook();
      } else if (this.addType === 'section') {
        this.createSection();
      } else if (this.addType === 'page') {
        this.createPage();
      }
      this.modalInput = '';
    },
    openEditNoteModal() {
      this.isEditNoteModalOpen = true;
      this.editNoteTitle = this.selectedNote.title;
      this.editNoteInput = this.noteContent;
      this.fetchNoteContent(this.selectedNote.contentUrl);
    },
    closeEditNoteModal() {
      this.isEditNoteModalOpen = false;
    },
    async saveNoteChanges() {
      const contentUrl = this.selectedNote.contentUrl;
      const commands = [
        {
          "target": "body",
          "action": "replace",
          "content": `<div id="divId" data-id="_default"><p>${this.editNoteInput}</p></div>`
        }
      ];

      const formData = new FormData();
      formData.append('commands', new Blob([JSON.stringify(commands)], { type: 'application/json' }));

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
        });

        const response = await fetch(contentUrl, {
          method: 'PATCH',
          headers,
          body: formData
        });

        if (!response.ok) {
          const errorBody = await response.text();
          console.error('Error body:', errorBody);
          throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }

        this.closeEditNoteModal();
        await this.fetchNoteContent(contentUrl);
        this.isEditNoteModalOpen = false;
      } catch (error) {
        console.error('Error updating note:', error);
      }
    },
    async handleDeleteButtonClick() {
      // Implémenter la logique de suppression ici
    },
    placeholders(count) {
      const placeholders = [];
      const itemsPerRow = 2;
      const remainder = count % itemsPerRow;
      if (remainder !== 0) {
        for (let i = 0; i < itemsPerRow - remainder; i++) {
          placeholders.push(i);
        }
      }
      return placeholders;
    }
  },
  mounted() {
    this.accessToken = localStorage.getItem('microsoft_access_token');
    if (!this.accessToken) {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has('access_token')) {
        this.accessToken = urlParams.get('access_token');
        localStorage.setItem('microsoft_access_token', this.accessToken);
        window.history.pushState({}, document.title, "/");
      } else {
        this.openMicrosoftLogin();
        return;
      }
    }
    this.fetchNotebooks();
  }
};
</script>


<style scoped>
@import '@vueup/vue-quill/dist/vue-quill.snow.css';

.bg-blue-200 {
  background-color: #bfdbfe;
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.my-button {
  background-color: #2176FF;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 10px;
  transition: background-color 0.3s ease;
  min-width: 200px;
  min-height: 50px;
}

.my-button:hover {
  background-color: #FFA93E;
}

.note-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.note-card {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  background-color: white;
  padding: 20px;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 45%;
  cursor: pointer;
  color: black;
  overflow-wrap: break-word;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.note-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.note-card.placeholder {
  visibility: hidden;
}

.note-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 0;
  color: #2176FF;
  cursor: pointer;
  transition: color 0.3s ease;
}

.note-title:hover {
  color: #FFA93E;
}

.note-content {
  text-align: justify;
  line-height: 1.6;
  white-space: pre-wrap;
  color: black;
  font-size: 18px;
  line-height: 1.6;
  padding: 16px;
  position: relative;
  top: 0;
  left: 0;
}

.note-detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 20px;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: none;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input, .textarea {
  width: 100%;
  padding: 8px;
  margin: 8px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.textarea {
  height: 150px;
}

.save-button, .cancel-button {
  margin-top: 10px;
}

.edit-button {
  margin-top: 10px;
}

.editor {
  background-color: white;
  border-radius: 8px;
  padding: 16px;
  width: 100%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.edit-note-modal {
  width: 100%;
    height: 90vh;
    text-align: -webkit-center;
    color: black;
}

.ql-editor {
    width: 100%;
    height: 1000px;
}

.ql-container {
    border-top: 1px solid #d1d5db !important;
    box-sizing: border-box;
    font-family: Helvetica, Arial, sans-serif;
    font-size: 13px;
    height: 100%;
    margin: 0px;
    position: relative;
    width: 100%;
}

.ql-toolbar.ql-snow {
    border: 1px solid #d1d5db;
    box-sizing: border-box;
    font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    padding: 8px;
    width: 100%;
}
</style>
