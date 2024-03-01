<template>
  <sidebar :activeButton="'caspratiques'"/>
  <div class="bg-[#F3F8FF] flex flex-row justify-center ml-[275px]">
    <div class="flex flex-col gap-[28px]">
      <div class="bg-[#FCD19C] w-[881px] h-[154px] rounded-[10px] mr-[62px] mt-[37px]"> 
        <h5 class=""> Que recherchez vous ?</h5>
        <input type="text" class="bg-[#F3F8FF] w-[255px] h-[37.696px] rounded-[10px] mr-[62px] mt-[37px]" value="Rechercher">
        <img src="./../assets/Bonhommecp.png">
      </div>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
      <class_casparatique/>
    </div>
  </div>

</template>


<script>
import sidebar from './../components/sidebar.vue';
import class_casparatique from './../components/class_caspratique.vue';

export default {
  name: 'caspratique',
  components: {
    sidebar,
    class_casparatique,
  },
  data() {
    return {
      isLightTheme: true,
    };
  },
  }

</script>
