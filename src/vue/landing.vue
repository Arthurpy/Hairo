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
        isMenuOpen: false,
      };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
}
</script>

<template>
  <div class="bg-white text-primary min-h-screen max-w-none">
    <div class="navbar bg-transparent fixed z-10">
      <div class="navbar-start text-secondary font-bold">
        <a class="navbar-item"> </a>
      </div>
      <div class="nabbar-center">
        <a class="navbar-item flex flex-row flex-end">
          <img src="../assets/images/logo.png" alt="logo" />
          <h2 class="text-2xl mt-2 ml-1 font-bold text-[#2176FF]">AIRO</h2>
        </a>
      </div>
      <div class="navbar-end">
        <div>
          <!-- Burger Menu for Mobile -->
          <div class="md:hidden">
            <button @click="toggleMenu" class="p-4">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
              </svg>
            </button>
            <div v-if="isMenuOpen" class="flex flex-col space-y-4 p-4">
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

          <!-- Square Buttons for Desktop -->
          <div class="hidden md:flex space-x-4">
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
      </div>
    </div>
    <div class="bg-white">
      <We/>
      <What/>
      <About/>
      <Testimonials/>
      <Footer/>
    </div>
  </div>
</template>
