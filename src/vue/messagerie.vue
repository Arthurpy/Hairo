<template>
    <sidebar :activeButton="'messagerie'"/>
    <div class="bg-blue-200 flex">
        <div class="flex flex-col ml-80">
    <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
      <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Messagerie</h1>
    </div>
  </div>
    <div class="main-content h-screen" style="display: flex; flex-direction: column; justify-content: center; align-items: center; max-width: 800px; margin: auto;">
    </div>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';

export default {
    name: 'messagerie',
    components: {
        sidebar,
    },
};
</script>

<style scoped>
</style>