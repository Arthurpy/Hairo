<template>
    <div class="flex justify-between">
        <sidebar :activeButton="'dashboard'"/>
        <div class="w-full h-screen bg-[#F3F8FF] p-4">
            <div class="flex items-center pb-8">
                <div class="w-full h-28 rounded-lg bg-[#FCD19C] flex justify-between items-center text-white text-center text-2xl font-bold">
                    Vos exploits en résumé  !
                    <button @click="goTofiche" class="flex justify-center items-center w-34 h-12 bg-blue-600 rounded-lg text-white">
                        ajouter une fiche
                    </button>
                    <img class="w-36 h-36 -rotate-10 shrink-0" src="../assets/megaphone.png">
                </div>
            </div>
            <div class="flex items-center pb-8 space-x-8">
                <div class="w-128 h-32 rounded-lg bg-[#D2EADA] space-x-5">
                    <p class="text-black text-center text-lg font-bold">
                        Bonjour Doe,
                    </p>
                    <p class="text-black text-center text-lg font-medium whitespace-normal">
                        Vous avez fournis de très beaux efforts ces derniers temps continuiez ainsi.
                    </p>
                </div>
                    <resultatqcm :value="43" />
                    <resultatqcm :value="56" />
            </div>
            <div class="flex items-center pb-8 space-x-5">
                <div class="w-1/3 h-32 bg-[#B4E1FE80] rounded-lg">
                    <h1>test 1</h1>
                </div>
                <div class="w-1/3 h-32 bg-[#B4E1FE80] rounded-lg">
                    <h1>test 2</h1>
                </div>
                <div class="w-1/3 h-32 bg-[#B4E1FE80] rounded-lg">
                    <h1>test 3</h1>
                </div>
            </div>
        </div>
        <profil/>
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import resultatqcm from '../components/resultatqcm.vue';
import profil from '../components/profil.vue';

export default {
    name: 'Dash',
    components: {
        sidebar,
        resultatqcm,
        profil,
    },
    methods: {
        goTofiche() {
            this.$router.push('/fiche');
        },
    }
};
</script>
