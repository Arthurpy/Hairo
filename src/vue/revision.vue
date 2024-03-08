<template>
    <div class="bg-[#F4FBFF] flex">
        <sidebar :activeButton="'revisions'"/>
        <div class="flex flex-col">
            <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
                <h4> Révisions </h4>
            </div>
            <div class="bg-black w-[70vw] h-[91px] rounded-lg mt-[30px] ml-[50px]">
                que rechercher vous?
            </div>
            <div class="flex flex-row ml-[50px] mt-[10px] h-[142px] space-x-[23px]">
                <div class="bg-[#2176FF] w-[100%] rounded-lg">
                    theme
                </div>
            </div>
            <div class="flex flex-row ml-[50px] mt-[10px] h-[142px] space-x-[23px]">
                <div class="bg-[#2176FF] w-[100%] rounded-lg">
                    theme
                </div>
            </div>
        </div>
    </div>
  </template>





<script>
  import sidebar from './../components/sidebar.vue';

  export default {
    name: 'revisions',
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
