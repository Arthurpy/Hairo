<template>
  <div class="bg-[#F4FBFF] flex">
    <sidebar :activeButton="'ressources'"/>
    <div class="flex flex-col">
      <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
        <h4> Révisions </h4>
      </div>
      <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px] flex items-center text-base p-[15px]">
        que rechercher vous?
        <input type="text" v-model="searchQuery" class="ml-[50px] mt-[10px] p-[5px] rounded-lg w-[75%]">
      </div>
      <p class="text-black ml-[50px] mt-[30px]"> Thème adapté à vos exam</p>
      <!-- Divisez la liste des cours en sous-listes de 4 éléments chacune -->
      <div v-for="(row, rowIndex) in filteredChunkedCourses" :key="rowIndex" class="flex flex-row ml-[50px] mt-[10px] space-x-[23px] h-[273px]">
        <!-- Parcourez chaque sous-liste pour afficher les cours -->
        <router-link v-for="(course, index) in row" :key="index" :to="{ name: 'CourseDetails', params: { courseName: course } }" class="bg-[#2176FF] w-[25%] rounded-lg">
          {{ course }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from './../components/sidebar.vue';
import pacesFolders from './../assets/pacesFolders.json';

export default {
  name: 'ressources',
  components: {
    sidebar,
  },
  data() {
    return {
      isLightTheme: true,
      courses: pacesFolders,
      searchQuery: '',
    };
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