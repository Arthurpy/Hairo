<script>
  import Testimonials from './components/test.vue';
  import We from './components/wee.vue';
  import What from './components/wwaht.vue';
  import About from './components/abo.vue';
  import Footer from './components/foot.vue';

  export default {
    name: 'App',
    components: {
    We,
    What,
    About,
    Testimonials,
    Footer
},
data() {
    return {
      isLightTheme: true,
    };
  },
  }
</script>

<template>
  <router-view></router-view>
</template>

<style>
body {
  font-family: 'Poppins', sans-serif;
}
</style>
