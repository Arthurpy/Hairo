<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'ressources'"/>
    <div class="flex flex-col ml-80">
      <div>
        <div class="flex mt-[40px] bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-center items-center">
          <h4 class="text-3xl font-bold"> {{ courseName }} </h4>
        </div>
        <div class="bg-white text-[#2176FF] w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px] flex items-center text-base p-[15px]">
          <h1 class="text-[#2176FF] text-2xl font-semibold">Que recherchez-vous ?</h1>
          <input type="text" v-model="searchQuery" class="input-rounded input ml-56" placeholder="Rechercher un thème">
        </div>
        <div class="flex flex-wrap ml-[50px] mt-[10px]">
          <router-link v-for="(file, index) in pdfFiles" :key="index" :to="{ name: 'ReadCours', params: { courseName: courseName, fileName: file } }" class="bg-[#2176FF] w-[21.5%] rounded-lg m-2">
            <div class="rounded-t-lg overflow-hidden">
              <img src="../assets/Anat.jpeg" alt="Aperçu PDF" class="w-full"/>
            </div>
            <h1 class="text-white font-semibold text-2xl mx-2 p-2 items-center"> {{ removePdfExtension(file) }} </h1>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from './../components/sidebar.vue';
import pdfFilesData from '../assets/PACES/course.json'; // Assurez-vous que le chemin d'accès est correct
import pacesFolders from './../assets/pacesFolders.json';


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
      courses: pacesFolders,
      searchQuery: '',
    };
  },
  mounted() {
    this.loadPdfFiles();
  },
  methods: {
    loadPdfFiles() {
      if (pdfFilesData[this.courseName] && pdfFilesData[this.courseName].fichiers) {
        this.pdfFiles = pdfFilesData[this.courseName].fichiers;
      } else {
        console.error(`Les fichiers pour le cours "${this.courseName}" n'existent pas dans le JSON.`);
      }
    },
    removePdfExtension(fileName) {
      return fileName.split('.')[0]; // Récupérer le nom du fichier avant le premier point (.)
    }
  },
  computed: {
    chunkedCourses() {
      const chunkSize = 4;
      const chunkedArray = [];
      for (let i = 0; i < this.courses.length; i += chunkSize) {
        chunkedArray.push(this.courses.slice(i, i + chunkSize));
      }
      return chunkedArray;
    },
    filteredCourses() {
      const query = this.searchQuery.toLowerCase();
      return this.courses.filter(course => course.toLowerCase().includes(query));
    },
    filteredChunkedCourses() {
      const chunkSize = 4;
      const chunkedArray = [];
      for (let i = 0; i < this.filteredCourses.length; i += chunkSize) {
        chunkedArray.push(this.filteredCourses.slice(i, i + chunkSize));
      }
      return chunkedArray;
    },
  },
};
</script>
