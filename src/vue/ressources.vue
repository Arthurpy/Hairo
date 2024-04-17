<template>
  <div class="bg-[#F4FBFF] flex w-[100vw] min-h-screen">
    <sidebar :activeButton="'ressources'"/>
    <div class="flex flex-col ml-80">
      <div class="flex flex-row bg-white rounded-2xl mt-4 ml-12 jus">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-20">Ressources</h1>
        <img src="../assets/book.png" alt="search" class="pb-8  w-auto ml-96" />
      </div>
      <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px] flex items-center text-base p-[15px]">
        Que recherchez-vous ?
        <input type="text" v-model="searchQuery" class="ml-[50px] mt-[10px] p-[5px] rounded-lg w-[75%]">
      </div>
      <p class="text-black ml-[50px] mt-[30px]"> Thème adapté à vos examens</p>
      <div v-for="(row, rowIndex) in filteredChunkedCourses" :key="rowIndex" class="flex flex-row ml-[50px] mt-[10px] space-x-[23px] h-[273px]">
        <router-link v-for="(course, index) in row" :key="index" :to="{ name: 'CourseDetails', params: { courseName: course.nom } }" class="bg-[#2176FF] w-[23%] rounded-lg">
          {{ course.nom }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import sidebar from './../components/sidebar.vue';

export default {
  name: 'ressources',
  components: {
    sidebar,
  },
  data() {
    return {
      courses: [],
      searchQuery: '',
    };
  },
  created() {
    this.fetchCourses();
  },
  methods: {
    fetchCourses() {
      axios.post('http://localhost:8000/api/cours/')
        .then(response => {
          this.courses = response.data;
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
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
      return this.courses.filter(course => course.nom.toLowerCase().includes(query));
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


<!-- <template>
  <div v-for="course in courses" :key="course.id" class="course-item">
    <router-link :to="{ name: 'CourseDetails', params: { courseId: course.id }}">
      {{ course.nom }}
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [],
    };
  },
  created() {
    this.fetchCourses();
  },
  methods: {
    fetchCourses() {
      axios.post('/api/cours/')  // Adjust this URL to your actual API endpoint
        .then(response => {
          this.courses = response.data;
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    }
  }
};
</script> -->
