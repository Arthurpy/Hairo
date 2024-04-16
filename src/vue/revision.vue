<template>
    <div class="bg-[#D2E3FF] flex">
        <sidebar :activeButton="'revisions'"/>
        <div class="flex flex-col">
            <SearchBar/>
            <div class="flex mt-[4% ml-[5%] flex-col px-12 mt-5 ">
                <div class="bg-white text-[#2176FF] w-[100%] rounded-lg">
                    bon 
                </div>
            </div>
        </div>
    </div>
  </template>





<script>
  import sidebar from './../components/sidebar.vue';
  import SearchBar from './../components/SearchComponent.vue';

  export default {
    name: 'revisions',
    components: {
      sidebar,
      SearchBar,
    },
    data() {
      return {
        isLightTheme: true,
      };
    },
    }

</script>
