<!-- <template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'revisions'" />
    <div class="flex flex-col ml-80 h-screen">
      <SearchBar />
      <div
        v-for="(revision, index) in myRevision"
        :key="index"
        class="flex ml-[5%] flex-col mt-5 bg-white text-[#2176FF] border-b-8 border-r-8 border-[#2176FF] rounded-3xl relative" 
      >
          <div class="flex justify-center">
            <p class="card-header justify-center bg-[#2176FF] rounded-b-xl flex text-white w-48">{{ revision.prog }}</p>
          </div>
          <div class="flex items-center">
            <h3 class="text-xl font-semibold mb-2 card-body mr-96 justify-start">{{ revision.titre }}</h3>
            <img :src="revision.img_src" alt="Image" class="w-20 h-20 justify-center" />
          </div>
          <div class="absolute top-2 right-2">
            <div
              :href="revision.red"
              class="flex hover:text-blue-200 text-white p-2 bg-[#2176FF] rounded-full cursor-pointer"
            >GO</div>
          </div>
          <div class="flex m-3 text-black justify-start items-start">
            <p class="mb-1 mx-11">Temps de formation: {{ revision.temp_form }}</p>
            <p class="mb-1">Nombre de questions: {{ revision.nbr_qcm }}</p>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from './../components/sidebar.vue';
import SearchBar from './../components/SearchComponent.vue';

export default {
  name: 'revisions',
  components: {
    sidebar,
    SearchBar,
  },
  data() {
    return {
      myRevision: [
        {prog: "60%", red: "https://example.com", temp_form: "30 min", nbr_qcm: "15", titre: "Biologie cellulaire", img_src: "src/assets/coeur.png"},
        {prog: "75%", red: "https://example.com", temp_form: "45 min", nbr_qcm: "20", titre: "Anatomie humaine", img_src: "../anatomy"},
        {prog: "50%", red: "https://example.com", temp_form: "40 min", nbr_qcm: "12", titre: "Biochimie structurale", img_src: "../biochemistry"},
        {prog: "80%", red: "https://example.com", temp_form: "50 min", nbr_qcm: "18", titre: "Physiologie humaine", img_src: "../physiology"},
        {prog: "65%", red: "https://example.com", temp_form: "35 min", nbr_qcm: "14", titre: "Histologie", img_src: "../histology"},
        {prog: "55%", red: "https://example.com", temp_form: "25 min", nbr_qcm: "10", titre: "Chimie générale", img_src: "../chemistry"},
        {prog: "70%", red: "https://example.com", temp_form: "50 min", nbr_qcm: "16", titre: "Embryologie", img_src: "../embryology"},
        {prog: "45%", red: "https://example.com", temp_form: "30 min", nbr_qcm: "12", titre: "Biophysique", img_src: "../biophysics"}
      ]
    };
  },
};
</script> -->



<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'revisions'" />
    <div class="flex flex-col ml-80 h-screen">
      <SearchBar />
      <div
        v-for="(revision, index) in myRevision"
        :key="index"
        class="flex ml-[5%] flex-col mt-5 bg-white text-[#2176FF] border-b-8 border-r-8 border-[#2176FF] rounded-3xl relative" 
      >
          <div class="flex justify-center">
            <p class="card-header justify-center bg-[#2176FF] rounded-b-xl flex text-white w-48">{{ revision.prog }}</p>
          </div>
          <div class="flex items-center">
            <h3 class="text-xl font-semibold mb-2 card-body mr-96 justify-start">{{ revision.titre }}</h3>
            <img :src="revision.img_src" alt="Image" class="w-20 h-20 justify-center" />
          </div>
          <div class="absolute top-2 right-2">
            <div
              :href="revision.red"
              class="flex hover:text-blue-200 text-white p-2 bg-[#2176FF] rounded-full cursor-pointer"
            >GO</div>
          </div>
          <div class="flex m-3 text-black justify-start items-start">
            <p class="mb-1 mx-11">Temps de formation: {{ revision.temp_form }}</p>
            <p class="mb-1">Nombre de questions: {{ revision.nbr_qcm }}</p>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import sidebar from './../components/sidebar.vue';
import SearchBar from './../components/SearchComponent.vue';

export default {
  name: 'revisions',
  components: {
    sidebar,
    SearchBar,
  },
  data() {
    return {
      myRevision: []
    };
  },
  mounted() {
    this.loadRevisions();
  },
  methods: {
    loadRevisions() {
    axios.get('http://localhost:8000/api/qcms/names')
        .then(response => {
            this.myRevision = response.data.map(qcm => ({
                prog: qcm.prog,
                red: qcm.red,
                temp_form: qcm.temp_form,
                nbr_qcm: qcm.nbr_qcm,
                titre: qcm.titre,
                img_src: qcm.img_src
            }));
        })
        .catch(error => {
            console.error("Error loading the revisions: ", error.response);
        });
}
  }
};
</script>
