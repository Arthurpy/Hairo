<script>
  import Testimonials from '../components/testimonials.vue';
  import We from '../components/We.vue';
  import What from '../components/What.vue';
  import About from '../components/about.vue';
  import Footer from '../components/Flutteur.vue';

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
          <img src="images/logo.png" alt="logo" />
          <h2 class="text-2xl mt-2 ml-1 font-bold text-[#2176FF]">AIRO</h2>
        </a>
      </div>
      <div class="navbar-end">
        <a class="navbar-item">
          <img src="images/insta.svg" alt="instagram" />
        </a>
        <a class="navbar-item">
          <img src="images/facebook.svg" alt="facebook" />
        </a>
        <a class="navbar-item">
          <img src="images/linkedin.svg" alt="linkedin" />
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