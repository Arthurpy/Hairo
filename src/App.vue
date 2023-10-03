<script>
  import Testimonials from './components/Testimonials.vue';
  import We from './components/We.vue';
  import What from './components/What.vue';
  import About from './components/about.vue';

  export default {
    name: 'App',
    components: {
    We,
    What,
    About,
    Testimonials,
}
  }
</script>

<template>
  <div class="flex justify-between py-10">
    <div class="flex mx-2">
      <text class="flex mx-2 p-2 font-bold">Home</text>
      <text class="flex mx-2 p-2">About Us</text>
      <text class="flex mx-2 p-2">Contatc Us</text>
    </div>
    <div class="flex">
      <img src="./assets/logo.svg" />
    </div>
    <div class="flex mx-2">
      <text class="flex p-2 border m-2 border-black rounded-lg">insta</text>
      <text class="flex p-2 border m-2 border-black rounded-lg">linkedin</text>
      <text class="flex p-2 border m-2 border-black rounded-lg">facebook</text>
      <text class="flex p-2 border m-2 border-black rounded-lg">X</text>
    </div>
  </div>
  <div>
    <We/>
    <What/>
    <About/>
    <Testimonials/>
  </div>
</template>
