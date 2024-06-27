<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'notes'"/>
    <div class="flex flex-col ml-80 flex-grow justify-center items-center">
      <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Mes notes</h1>
      </div>
      <div class="main-content h-screen flex flex-col items-center">
        <div style="display: flex;">
        <button @click="handleAddButtonClick" class="add-button my-button">Ajouter</button>
        <button @click="handleDeleteButtonClick" class="delete-button my-button">Supprimer</button>
        </div>
        <template v-if="!selectedNotebook">
    <div v-for="notebook in notebooks" :key="notebook.id" class="note-card bg-white p-4 m-4 rounded-lg shadow-md w-[60vw]">
      <input type="checkbox" :value="notebook.id" v-model="selectedItemId">
      <h2 class="note-title text-2xl font-bold mb-2" @click="selectNotebook(notebook)">{{ notebook.displayName }}</h2>
    </div>
  </template>
  <template v-else-if="selectedNotebook && !selectedSection">
    <div v-for="section in sections[selectedNotebook.id]" :key="section.id" class="note-card bg-white p-4 m-4 rounded-lg shadow-md w-[60vw]">
      <input type="checkbox" :value="section.id" v-model="selectedItemId">
      <h2 class="note-title text-2xl font-bold mb-2" @click="selectSection(section)">{{ section.displayName }}</h2>
    </div>
  </template>
  <template v-else-if="selectedSection && !selectedNote">
    <div v-for="note in notes" :key="note.id" class="note-card bg-white p-4 m-4 rounded-lg shadow-md w-[60vw]">
      <input type="checkbox" :value="note.id" v-model="selectedItemId">
      <h2 class="note-title text-2xl font-bold mb-2" @click="selectNote(note)">{{ note.title }}</h2>
    </div>
  </template>
        <template v-else>
          <div class="note-detail bg-blue-200 flex flex-col items-center h-screen w-full">
            <div class="note-card bg-white p-4 m-4 rounded-lg shadow-md w-[60vw]">
              <div class="flex flex-col">
                <h2 class="note-title text-2xl font-bold mb-2">{{ selectedNote.title }}</h2>
                <div class="note-content p-4 text-justify" v-html="noteContent"></div>
              </div>
            </div>
            <div class="flex">
              <button @click="openEditNoteModal" class="edit-button my-button">Modifier</button>
              <button @click="deselectNote" class="back-button my-button">Retour aux pages</button>
            </div>
          </div>
        </template>
        <template v-if="selectedNotebook || selectedSection || selectedNote">
          <div style="display: flex;">
          <button @click="deselectNotebook" class="back-button my-button">Retour aux notebooks</button>
          <button @click="deselectSection" class="back-button my-button">Retour à la section</button>
          </div>
        </template>
      <div v-if="isEditNoteModalOpen" class="edit-note-modal">
        <div class="modal-content">
          <h2>Modifier la note</h2>
          <input type="text" v-model="editNoteTitle" placeholder="Titre de la note"/>
          <textarea v-model="editNoteInput" placeholder="Contenu de la note"></textarea>
          <button @click="saveNoteChanges" class="save-button my-button">Sauvegarder</button>
          <button @click="closeEditNoteModal" class="cancel-button my-button">Annuler</button>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import { reactive } from 'vue';

export default {
  name: 'notes',
  components: {
    sidebar
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
        if (response.status === 401) {
          localStorage.removeItem('microsoft_access_token');
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
      url = data['@odata.nextLink']; // URL de la page suivante si elle existe
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
      url = data['@odata.nextLink']; // URL de la page suivante si elle existe
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
      'Content-Type': 'application/json'
    });
    const response = await fetch(contentUrl, { headers });
    if (!response.ok) {
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }
    const content = await response.text();
    console.log('Note content:', content)
    return content;
  } catch (error) {
    console.error('Error fetching note content:', error);
    return '';
  }
},

    handleAddButtonClick() {
  if (this.selectedNotebook && !this.selectedSection) {
    this.createSection();
  } else if (this.selectedSection && !this.selectedNote) {
    this.createPage();
  } else if (!this.selectedNotebook) {
    this.createNotebook();
  }
},
    async createSection() {
      const sectionName = prompt('Nom de la section:');
      if (!sectionName) return;

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        const body = JSON.stringify({
          'displayName': sectionName
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
      const pageTitle = prompt("Titre de la nouvelle page:");
      if (!pageTitle) return;

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
          <title>${pageTitle}</title>
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
      const notebookName = prompt('Nom du notebook:');
      if (!notebookName) return;

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json'
        });
        const url = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks';
        const body = JSON.stringify({
          'displayName': notebookName
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
    async openEditNoteModal() {
  this.isEditNoteModalOpen = true;
  this.editNoteTitle = this.selectedNote.title;
  this.editNoteInput = await this.fetchNoteContent(this.selectedNote.contentUrl);
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
  } catch (error) {
    console.error('Error updating note:', error);
  }
},
async handleDeleteButtonClick() {
  },

  },
  async mounted() {
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
  },
};
</script>

<style scoped>
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
}

.my-button:hover {
  background-color: #FFA93E;
  border-radius: 20px;
}

.add-button {
  margin-top: 20px;
  align-self: flex-start;
  margin-left: 80px;
}

.note-card {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  background-color: white;
  padding: 20px;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 70vw;
  max-width: 800px;
  cursor: pointer;
  color: black;
  overflow-wrap: break-word;
}

.note-title {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 16px;
  color: black;
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
  width: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.save-button, .cancel-button {
  margin-top: 10px;
}

.edit-button {
  margin-top: 10px;
}
</style>
