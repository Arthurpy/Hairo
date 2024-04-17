   <!-- <template>
    <div class="bg-[#F4FBFF] flex">
      <sidebar :activeButton="'ressources'"/>
      <div class="flex flex-col ml-80">
        <div>
          <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
            <h4> Révisions </h4>
          </div>
          <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
            que rechercher vous?
          </div>
          <h2 class="">{{ courseName }}</h2>
          <div class="flex flex-wrap ml-[50px] mt-[10px]">
            <router-link v-for="(file, index) in pdfFiles" :key="index" :to="{ name: 'ReadCours', params: { courseName: courseName, fileName: file } }" class="bg-[#2176FF] w-[25%] rounded-lg mb-[10px] h-[273px] m-8">{{ file }}</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import sidebar from './../components/sidebar.vue';
  
  export default {
    components: {
    sidebar
  },
    data() {
      return {
        courseDetails: null
      };
    },
    mounted() {
    this.fetchCourseDetails();
  },
  methods: {
    fetchCourseDetails() {
      const courseName = this.$route.params.courseName; // Assume this still comes from the route
      axios.post('http://localhost:8000/api/course-details-by-name/', { courseName: courseName })
        .then(response => {
          this.courseDetails = response.data;
          console.log("Course details received:", this.courseDetails);
        })
        .catch(error => {
          console.error('Error fetching course details by name:', error);
          this.courseDetails = null;
        });
    }
  }

  };
  </script> -->


   <template>
    <sidebar :activeButton="'ressources'"/>
    <div v-if="courseDetails">
      <h1>{{ courseDetails.nom }}</h1>
      <ul>
        <li v-for="pdf in courseDetails.pdfs" :key="pdf.id">
          <a :href="pdf.url" target="_blank">{{ pdf.nom }}</a>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Loading course details or course not found...</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import sidebar from './../components/sidebar.vue';
  
  export default {
    components: {
    sidebar
  },
    data() {
      return {
        courseDetails: null
      };
    },
    mounted() {
    this.fetchCourseDetails();
  },
  methods: {
    fetchCourseDetails() {
      const courseName = this.$route.params.courseName; // Assume this still comes from the route
      axios.post('http://localhost:8000/api/course-details-by-name/', { courseName: courseName })
        .then(response => {
          this.courseDetails = response.data;
          console.log("Course details received:", this.courseDetails);
        })
        .catch(error => {
          console.error('Error fetching course details by name:', error);
          this.courseDetails = null;
        });
    }
  }

  };
  </script>
  