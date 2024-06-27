<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'ressources'"/>
    <div class="flex flex-col ml-80">
      <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Ressources</h1>
        <img src="../assets/book.png" alt="search" class="w-auto" />
      </div>
      <div class="flex">
        <div class="bg-white text-[#2176FF] w-[50vw] h-auto rounded-lg mt-[30px] ml-[50px] flex items-center text-base p-[15px]">
          <h1 class="text-[#2176FF] text-2xl font-semibold">Que rechercher vous?</h1>
          <input type="text" v-model="searchQuery" class="input-rounded input ml-56" style="color: white;" placeholder="Rechercher un thème">
        </div>
        <div class="recommended-courses bg-white text-[#2176FF] w-[18vw] h-auto rounded-lg mt-[30px] ml-[20px] p-[15px]">
          <h2 class="text-[#2176FF] text-xl font-semibold">Cours conseillés</h2>
          <div style="display: flex;">
            <div v-for="(course, index) in recommendedCourses" :key="index" :to="{ name: 'CourseDetails', params: { courseName: course } }" class="recommended-course bg-[#2176FF] text-white rounded-lg p-2 mt-2">
              {{ course }}
            </div>
          </div>
        </div>
      </div>
      <div v-for="(row, rowIndex) in filteredChunkedCourses" :key="rowIndex" class="flex flex-row ml-[50px] mt-[10px] h-[200px]">
        <router-link v-for="(course, index) in row" :key="index" :to="{ name: 'CourseDetails', params: { courseName: course.name } }" class="bg-[#2176FF]  w-[21.5%] rounded-lg m-2 flex flex-col items-center justify-center p-4">
          <div class="text-white font-semibold text-5xl mb-2">{{ course.count }} cours</div>
          <h1 class="text-white font-semibold text-2xl mx-2 p-2 items-center"> {{ course.name }} </h1>
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
      recommendedCourses: ['Anat', 'Génome', 'Biomol'] // Vos cours conseillés
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
      return this.courses.filter(course => course.name.toLowerCase().includes(query));
    },
    filteredChunkedCourses() {
      const chunkSize = 4;
      const chunkedArray = [];
      for (let i = 0; i < this.filteredCourses.length; i += chunkSize) {
        chunkedArray.push(this.filteredCourses.slice(i, i + chunkSize));
      }
      return chunkedArray;
    }
  },
};
</script>


<style>

.bg-blue-200 {
  background-color: #bfdbfe;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.justify-between {
  justify-content: space-between;
}

.items-center {
  align-items: center;
}

.mt-10 {
  margin-top: 2.5rem;
}

.py-16 {
  padding-top: 4rem;
  padding-bottom: 4rem;
}

.search-title {
  font-size: 2.5rem;
}

.w-auto {
  width: auto;
}

.h-[91px] {
  height: 91px;
}

.mt-[30px] {
  margin-top: 30px;
}

.ml-[20px] {
  margin-left: 20px;
}

.ml-56 {
  margin-left: 14rem;
}

.input-rounded {
  border-radius: 9999px;
}

.p-[15px] {
  padding: 15px;
}

.text-base {
  font-size: 1rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.font-semibold {
  font-weight: 600;
}

.recommended-courses {
  display: flex;
  flex-direction: column;
}

.recommended-course {
  padding: 1rem;
  width: 33%;
  font-size: smaller;
  display: flex;
  justify-content: center;
  margin: auto;
}

.text-xl {
  font-size: 1.25rem;
}

.mt-2 {
  margin-top: 0.5rem;
}


</style>