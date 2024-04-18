
<template>
  <div>
    <sidebar :activeButton="'ressources'" @openNoteTaker="openNoteTaker" />
    <div class="main-content">
      <div class="pdf-container" v-if="selectedPdfUrl" ref="pdfContainer">
        <embed :src="selectedPdfUrl" type="application/pdf" width="80%" height="600px" class="ml">
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
        console.log("Loading PDF...");
        this.selectedPdfUrl = `http://localhost:8000/media/${this.fileName}`;
        console.log("fileName:", this.fileName)
        console.log("Loaded PDF URL:", this.selectedPdfUrl);
      }
    },
    mounted() {
      if (this.courseName && this.fileName) {
        this.loadPdf();
      }
    },
  };
  </script>
  