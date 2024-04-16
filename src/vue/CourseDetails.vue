<!-- <template>
    <div class="bg-[#F4FBFF] flex">
      <sidebar :activeButton="'ressources'"/>
      <div class="flex flex-col">
        <div>
          <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
            <h4> Révisions </h4>
          </div>
          <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
            que rechercher vous?
          </div>
          <h2 class="">{{ courseName }}</h2>
          <div class="flex flex-wrap ml-[50px] mt-[10px]">
            <a v-for="(file, index) in pdfFiles" :key="index" :href="getPdfFilePath(courseName, file)" target="_blank" class="bg-[#2176FF] w-[25%] rounded-lg mb-[10px] h-[273px] m-8">{{ file }}</a>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import sidebar from './../components/sidebar.vue';
  import pdfFilesData from '../assets/PACES/course.json'; // Remplacez le chemin par le chemin correct vers votre fichier JSON
  
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
        // Charger les noms des fichiers PDF pour le cours sélectionné à partir du fichier JSON
        this.pdfFiles = pdfFilesData[this.courseName] || [];
      },
      getPdfFilePath(courseName, fileName) {
        return `/assets/PACES/${courseName}/${fileName}`;
      },
    },
  };
  </script>
   -->

   <template>
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
          <!-- Afficher les fichiers PDF associés à ce cours -->
          <!-- Vous pouvez utiliser une boucle v-for pour afficher tous les fichiers PDF ici -->
          <div class="flex flex-wrap ml-[50px] mt-[10px]">
            <!-- Utilisation de Vue Router pour naviguer vers la page ReadCours.vue -->
            <router-link v-for="(file, index) in pdfFiles" :key="index" :to="{ name: 'ReadCours', params: { courseName: courseName, fileName: file } }" class="bg-[#2176FF] w-[25%] rounded-lg mb-[10px] h-[273px] m-8">{{ file }}</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import sidebar from './../components/sidebar.vue';
  import pdfFilesData from '../assets/PACES/course.json'; // Remplacez le chemin par le chemin correct vers votre fichier JSON
  
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
        // Charger les noms des fichiers PDF pour le cours sélectionné à partir du fichier JSON
        this.pdfFiles = pdfFilesData[this.courseName] || [];
      },
    },
  };
  </script>
  