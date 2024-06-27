<template>
    <div class="relative flex flex-row justify-between max-w-none">
      <div class="ml-20 mt-64 z-10">
        <h1 class="font-extrabold sm:text-7xl text-4xl">
          Tu as besoin d'aide
        </h1>
        <h1 class="sm:text-7xl text-4xl">
          pour réussir ton année?
        </h1>
        <p class="flex sm:text-xl text-sm w-9/12 mt-5">
          Booste ta réussite cette année avec une organisation optimale de tes révisions. Accède à tout moment à des ressources, cas pratiques, et reçois des retours personnalisés grâce à l'IA, des QCM, et des plans de révisions sur mesure.
        </p>
        <button @click="goToRegister" class="flex p-5 mt-16 bg-[#B4E1FE] px-7 rounded-lg uppercase font-bold my-4">
          nous rejoindre
        </button>
      </div>
      <div class="w-full hidden xl:flex">
        <img src="../assets/We.png" alt="We" class="object-contain"/>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'We',
    methods: {
      goToLogin() {
        this.$router.push('/login');
      },
      goToRegister() {
        this.$router.push('/register');
      },
    },
  };
  </script>