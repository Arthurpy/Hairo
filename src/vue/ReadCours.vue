User
<template>
    <div>
      <sidebar :activeButton="'ressources'" @openNoteTaker="openNoteTaker" />
      <div class="main-content">
        <div class="pdf-container" v-if="selectedPdfUrl" ref="pdfContainer">
            <iframe :src="selectedPdfUrl" width="100%" height="1000px" frameborder="1" scrolling="auto" sandbox="allow-scripts"></iframe>
        </div>
        <div v-else class="no-pdf-selected">
          <p>Aucun PDF sélectionné.</p>
        </div>
        <button @click="openNoteTaker" class="note-button">Ouvrir le bloc-notes</button>
      </div>
    </div>
  </template>
  
  <script>
  import sidebar from './../components/sidebar.vue';
  
  export default {
    name: 'ReadCours',
    components: {
      sidebar,
    },
    data() {
      return {
        selectedPdfUrl: null,
      };
    },
    methods: {
      openNoteTaker() {
        console.log("Ouvrir le composant de prise de notes");
      },
      loadPdf(courseName, fileName) {
        this.selectedPdfUrl = `/src/assets/PACES/${courseName}/${fileName}`;
        console.log("URL :", this.selectedPdfUrl);
        this.loadPdfPages();
      },
      loadPdfPages() {
        const loadingTask = pdfjsLib.getDocument(this.selectedPdfUrl);
        loadingTask.promise.then(pdf => {
          for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
            pdf.getPage(pageNum).then(page => {
              const scale = 1.5;
              const viewport = page.getViewport({ scale });
              const canvas = document.createElement('canvas');
              const context = canvas.getContext('2d');
              canvas.height = viewport.height;
              canvas.width = viewport.width;
              page.render({
                canvasContext: context,
                viewport: viewport
              }).promise.then(() => {
                this.$refs.pdfContainer.appendChild(canvas);
              });
            });
          }
        });
      }
    },
    mounted() {
      const urlSegments = this.$route.path.split('/');
      const courseName = urlSegments[urlSegments.indexOf('cours') + 1];
      const fileName = urlSegments[urlSegments.length - 1];
      if (courseName && fileName) {
        this.loadPdf(courseName, fileName);
      }
    },
  };
  </script>
  
  <style>
  .main-content {
    margin-left: 250px;
  }
  
  .pdf-container {
    margin: 20px;
  }
  
  .no-pdf-selected {
    text-align: center;
  }
  
  .note-button {
    margin-top: 20px;
  }
  </style>