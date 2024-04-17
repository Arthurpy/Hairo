<template>
  <div class="bg-[#F4FBFF] flex">
    <sidebar :activeButton="'ressources'"/>
    <div class="flex flex-col ml-80">
      <div>
        <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
          <h4> {{ courseName }} </h4>
        </div>
        <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
          Que recherchez-vous ?
        </div>
        <div class="flex flex-wrap ml-[50px] mt-[10px]">
          <router-link v-for="(file, index) in pdfFiles" :key="index" :to="{ name: 'ReadCours', params: { courseName: courseName, fileName: file } }" class="bg-[#2176FF] w-[21.5%] rounded-lg m-2">
            <div class="rounded-t-lg overflow-hidden">
              <img src="../assets/Anat.jpeg" alt="Aperçu PDF" class="w-full"/>
            </div>
            <h1 class="text-white font-semibold text-2xl mx-2 p-2 items-center"> {{ file }} </h1>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from './../components/sidebar.vue';
import pdfFilesData from '../assets/PACES/course.json'; // Assurez-vous que le chemin d'accès est correct

export default {
  name: 'CourseDetails',
  components: {
    sidebar,
  },
  props: {
    courseName: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      pdfFiles: [],
    };
  },
  mounted() {
    this.loadPdfFiles();
  },
  methods: {
    loadPdfFiles() {
      // Vérifie si le cours existe dans le JSON
      if (pdfFilesData[this.courseName] && pdfFilesData[this.courseName].fichiers) {
        this.pdfFiles = pdfFilesData[this.courseName].fichiers;
      } else {
        console.error(`Les fichiers pour le cours "${this.courseName}" n'existent pas dans le JSON.`);
      }
    },
  },
};
</script>
