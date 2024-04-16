<template>
    <div>
      <sidebar :activeButton="'ressources'" @openNoteTaker="openNoteTaker" />
      <div class="main-content">
        <div class="pdf-container" v-if="selectedPdfUrl">
          <embed :src="selectedPdfUrl" type="application/pdf" width="100%" height="1000px" />

        </div>
        <div v-else class="no-pdf-selected">
          <p>Aucun PDF sélectionné.</p>
        </div>
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
        // Logic to open the note taker component
        console.log("Open note taker");
      },
      loadPdf(courseName, fileName) {
        // Construire l'URL du PDF en utilisant le nom du fichier inclus dans l'URL
        this.selectedPdfUrl = `http://localhost:5173/assets/PACES/${courseName}/${fileName}`;
        console.log("url :", this.selectedPdfUrl);
      },
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
    margin-left: 250px; /* Adjust according to your sidebar width */
  }
  
  .pdf-container {
    margin: 20px;
  }
  
  .no-pdf-selected {
    text-align: center;
  }
  </style>