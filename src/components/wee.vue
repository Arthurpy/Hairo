<template>
    <div class="flex flex-row justify-between">
        <div class=" ml-20 mt-64" >
            <h1 class="font-extrabold text-7xl sm:">
                Tu as besoins d'aide 
            </h1>
            <h1 class="text-7xl">
                pour reussir ton année?
            </h1>
            <text class="flex text-xl w-9/12 mt-5">
                Booste ta réussite cette année avec une organisation optimale de tes révisions. Accède à tout moment à des ressources, cas pratiques, et reçois des retours personnalisés grâce à l'IA, des QCM, et des plans de révisions sur mesure.
            </text>
            <button @click="goToRegister" class="flex p-5 mt-16 bg-[#B4E1FE] px-7 rounded-lg uppercase font-bold my-4">
                nous rejoindre
            </button>
        </div>
        <div class="-mr-12 -mb-20  -z-1 w-full">
            <img src="../assets/We.png" alt="We"/>
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
}
</script>
