
<template>
  <div class="bg-white w-screen h-screen">
    <sidebar :activeButton="'ressources'"/>
    <div class="main-content bg-blue">
      <div class="pdf-container" v-if="selectedPdfUrl" ref="pdfContainer">
        <object :data="selectedPdfUrl" type="application/pdf" width="70%" class="ml-80 pt-20 h-screen">
          <button @click="openNoteTaker" class="black absolute top-0 right-0 mt-4 mr-4">Ouvrir le bloc-notes</button>
        </object>
        </div>
        <div v-else class="no-pdf-selected">
          <p>Aucun PDF sélectionné.</p>
        </div>
      </div>
      vcfd
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
        this.selectedPdfUrl = `http://localhost:8000/media/${this.fileName}`;
        console.log("Loaded PDF URL:", this.selectedPdfUrl);
      },
      openNoteTaker() {
        console.log("Opening note taker...");
      },
    },
    mounted() {
      if (this.courseName && this.fileName) {
        this.loadPdf();
      }
    },
  };
  </script>
  