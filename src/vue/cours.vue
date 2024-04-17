<template>
    <div class="bg-[#F4FBFF] flex">
        <sidebar :activeButton="'caspratiques'"/>
        <div class="flex flex-col ml-80">
            <div class="flex flex-row bg-white rounded-2xl mt-4">
                <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-20">Révision et préparation</h1>
                <img src="../assets/book.png" alt="search" class="pb-8  w-auto ml-96" />
            </div>
            <div class="flex flex-row bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
                <button> retour</button>
                <h4>Nom du themes </h4>
            </div>
            <p class="text-black ml-[50px] mt-[30px]"> Les chapitres</p>
            <div class="flex flex-row ml-[50px] mt-[10px] h-[273px] space-x-[23px]">
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
            </div>
            <p class="text-black ml-[50px] mt-[30px]"> Les exercices</p>
            <div class="flex flex-row ml-[50px] mt-[10px] h-[273px] space-x-[23px]">
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
                <div class="bg-[#2176FF] w-[25%] rounded-lg">
                    theme
                </div>
            </div>
        </div>
    </div>
  </template>





<script>
  import sidebar from './../components/sidebar.vue';

  export default {
    name: 'ressources',
    components: {
      sidebar,
    },
    data() {
      return {
        isLightTheme: true,
      };
    },
    }

</script>
