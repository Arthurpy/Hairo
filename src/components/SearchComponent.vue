<template>
    <div class="flex mt-[4% ml-[5%] flex-col text-[#2176FF] pr-12 mt-5 ">
      <div class="flex flex-row bg-white rounded-2xl justify-between">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center mx-5">Révision et préparation</h1>
        <img src="../assets/golmon.png" alt="search" class="-mt-5 pb-8  w-auto mx-5" />
      </div>
      <div class="flex flex-row bg-white z-10 p-5 px-5 mt-5 rounded-2xl">
        <h1 class=" text-2xl mx-10 mt-1">Que recherchez vous ?</h1>
        <div class="search-bar flex w-80 ml-56">
          <input class="input-rounded input" style="border-radius: 9999px 0px 0px 9999px; background: white; border: 1px solid black; border-right: 0px; color: white" placeholder="Rechercher un thème" />
          <button class="btn btn-warning" style="border-radius: 0px 9999px 9999px 0px; border: 1px solid black; border-left: 0px;">
            <img src="../assets/search.svg" class=""/>
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchSection',
    data() {
      return {
        searchTerm: ''
      };
    },
    methods: {
      onSearchInput() {
        this.$emit('search-input', this.searchTerm);
      },
      onSearchClick() {
        this.$emit('search-click', this.searchTerm);
      }
    }
  };
  </script>