<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'revisions'" />
    <div class="flex flex-col ml-80 bg-blue-200 flex mr-[3rem] mb-[50px]" style="width: -webkit-fill-available; margin-right: 5%;">
      <SearchBar />
      <div
        v-for="(revision, index) in myRevision"
        :key="index"
        class="flex ml-[5%] mr-[3rem] flex-col mt-5 bg-white text-[#2176FF] border-b-8 border-r-8 border-[#2176FF] rounded-3xl relative" 
      >
        <div class="flex justify-center">
          <p class="card-header justify-center bg-[#2176FF] rounded-b-xl flex text-white w-48">{{ revision.prog }}</p>
        </div>
        <div class="flex items-center" style="justify-content: space-between; margin-right: 100px;">
          <h3 class="text-xl font-semibold mb-2 card-body mr-96 justify-start">{{ revision.titre }}</h3>
          <img :src="revision.img_src" alt="Image" class="w-20 h-20 justify-center" />
        </div>
        <div class="absolute top-2 right-2">
          <router-link to="/Quiz" class="flex hover:text-blue-200 text-white p-2 bg-[#2176FF] rounded-full cursor-pointer">
            GO
          </router-link>
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
      axios.get('http://localhost:8000/qcms/names/')
        .then(response => {
          this.myRevision = response.data.map(qcm => ({
            prog: "60%",
            red: qcm.contenu_json,
            temp_form: "30 min",
            nbr_qcm: "20",
            titre: qcm.qcm_name,
            img_src: "src/assets/coeur.png"
          }));
        })
        .catch(error => {
          console.error("Error loading the revisions: ", error.response);
        });
    }
  }
};
</script>
