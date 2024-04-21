<template>
  <div class="bg-blue-200 flex">
    <sidebar :activeButton="'messagerie'"/>
    <div class="flex flex-col ml-80 flex-grow">
      <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Mes notes</h1>
      </div>
      <div class="main-content h-screen flex justify-center items-center">
        <img class="w-1/4 h-auto" src="../assets/workinprogress.png" style="margin-bottom: 150px;">
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';

export default {
    name: 'notes',
    components: {
        sidebar,
    }
}
</script>

<style scoped>
</style>