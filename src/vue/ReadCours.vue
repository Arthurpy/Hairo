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
    props: ['courseName', 'fileName'],
    data() {
      return {
        selectedPdfUrl: null,
      };
    },
    methods: {
      loadPdf() {
        this.selectedPdfUrl = `http://localhost:5173/src/assets/PACES/${this.courseName}/${this.fileName}`;
        console.log("Loaded PDF URL:", this.selectedPdfUrl);
        // ici, chargez et affichez le PDF comme vous le souhaitez
      }
    },
    mounted() {
      if (this.courseName && this.fileName) {
        this.loadPdf();
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