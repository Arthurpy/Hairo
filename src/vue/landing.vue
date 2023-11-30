<script>
  import Testimonials from '../components/test.vue';
  import We from '../components/wee.vue';
  import What from '../components/wwaht.vue';
  import About from '../components/abo.vue';
  import Footer from '../components/foot.vue';

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
  <div class="bg-white text-primary">
    <div class="navbar bg-backgroung fixed">
      <div class="navbar-start text-secondary font-bold">
        <a class="navbar-item">Home</a>
        <a class="navbar-item">About</a>
        <a class="navbar-item">Contact</a>
      </div>
      <div class="nabbar-center">
        <a class="navbar-item flex flex-row flex-end">
          <img src="../assets/images/logo.png" alt="logo" />
          <h2 class="text-2xl mt-2 ml-1 font-bold text-[#2176FF]">AIRO</h2>
        </a>
      </div>
      <div class="navbar-end">
        <a class="navbar-item">
          <img src="../assets/images/insta.svg" alt="instagram" />
        </a>
        <a class="navbar-item">
          <img src="../assets/images/facebook.svg" alt="facebook" />
        </a>
        <a class="navbar-item">
          <img src="../assets/images/linkedin.svg" alt="linkedin" />
        </a>
      </div>
    </div>
    <div class="bg-white">
      <We class=""/>
      <What/>
      <About/>
      <Testimonials/>
      <Footer/>
    </div>
  </div>
</template>
