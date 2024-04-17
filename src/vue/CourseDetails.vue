
  <template>
    <div class="bg-[#F4FBFF] flex w-[100vw] min-h-screen">
      <sidebar :activeButton="'ressources'"/>
      <div v-if="courseDetails" class="flex flex-col ml-80">
        <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
          <h4>{{ courseDetails.nom }}</h4>
        </div>
        <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
          Que recherchez-vous ?
          <input type="text" v-model="searchQuery" @input="filterPDFs" class="ml-[50px] mt-[10px] p-[5px] rounded-lg w-[75%]">
        </div>
        <div class="flex flex-wrap flex-row ml-[50px] mt-[10px]">
          <ul class="flex flex-wrap">
            <li v-for="pdf in filteredPDFs" :key="pdf.id" class="flex flex-row bg-[#2176FF] w-[23%] rounded-lg mb-[10px] h-[273px] m-8">
              <a @click="openPdf(courseDetails.nom, pdf.nom)" class="cursor-pointer">{{ pdf.nom }}</a>
            </li>
          </ul>
        </div>
      </div>
      <div v-else>
        <p>Loading course details or course not found...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import sidebar from './../components/sidebar.vue';
  import { useRouter } from 'vue-router';
  
  export default {
    components: {
      sidebar
    },
    data() {
      return {
        courseDetails: null,
        searchQuery: '',
        filteredPDFs: [],
      };
    },
    setup() {
      const router = useRouter();
      return { router };
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
            this.filteredPDFs = this.courseDetails.pdfs; // Initialize filteredPDFs with all PDFs
            console.log("Course details received:", this.courseDetails);
          })
          .catch(error => {
            console.error('Error fetching course details by name:', error);
            this.courseDetails = null;
          });
      },
      openPdf(courseName, fileName) {
        this.$router.push({ name: 'ReadCours', params: { courseName, fileName } });
      },
      filterPDFs() {
        const query = this.searchQuery.toLowerCase();
        this.filteredPDFs = this.courseDetails.pdfs.filter(pdf => pdf.nom.toLowerCase().includes(query));
      }
    }
  };
  </script>
  


