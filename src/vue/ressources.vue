<template>
    <div class="bg-[#F4FBFF] flex">
        <sidebar :activeButton="'ressources'"/>
        <div class="flex flex-col">
            <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
                <h4> Révisions </h4>
            </div>
            <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
                que rechercher vous?
            </div>
            <p class="text-black ml-[50px] mt-[30px]"> Thème adapté à vos exam</p>
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
            <p class="text-black ml-[50px] mt-[30px]"> Autres thèmes</p>
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
