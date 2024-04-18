<template>
    <div class="bg-blue-200 flex">
        <sidebar :activeButton="'dashboard'"/>
        <div class="flex flex-col ml-80 h-screen">
            <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
                <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Dashboard</h1>
                <img src="../assets/Rocket.png" alt="search" class="w-auto h-[150px] drop-shadow-lg" />
            </div>
            <div class="flex flex-row">
                <div class="flex flex-row bg-black w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg">
                    <div class="w-[50%]">
                        <h4> Dates proches</h4>
                    </div>
                    <div class="bg-[#2176FF] w-[50%] rounded-r-lg">
                        ffw
                    </div>
                </div>
                <div class="flex flex-col bg-white w-1/2 ml-[50px] mt-[30px] rounded-lg">
                    <div class="h-[70%] flex flex-row m-3 text-[#2176FF]">
                        <img src="../assets/PP.png" alt="profile" class="w-[70px] h-[70px]"/>
                        <div class="flex flex-col ml-4 mt-2">
                            <h4 class="font-bold text-[#FFA93E]">Arthur Py</h4>
                            <h4 class="">P1 2024</h4>
                        </div>
                        <div class="flex flex-col ml-4 mt-2">
                            <h4 class="font-bold text-[#FFA93E]">Moyenne</h4>
                            <h4 class="">12.5</h4>
                        </div>
                    </div>
                    <div class="flex flex-row justify-between text-[#2176FF] ">
                        <div class="mx-5 ">
                            <h4>Tutorat Médecine </h4>
                            <h4>FAC de Bordeaux Montesquieu</h4>
                        </div>
                        <div class=" mx-5">
                            <h4>Groupe 3</h4>
                            <h4>89/460</h4>
                        </div>
                    </div>
                    <div class="flex flex-row justify-around mb-4 mt-6">
                        <div class="flex btn bg-[#2176FF] font-semibold">voir le profil</div>
                        <div class="flex btn bg-[#2176FF] font-semibold">voir le profil</div>
                    </div>
                </div>
            </div>
            <div class="mt-[40px] bg-black w-[70vw] h-[205px] ml-[50px] rounded-lg">
                <h4> statistique </h4>
            </div>
            <div class="flex flex-row">
                <div class="flex flex-row bg-black w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg">
                    <div class="w-[65%]">
                        <h4> Dates proches</h4>
                    </div>
                    <div class="bg-[#2176FF] w-[35%] rounded-r-lg">
                        ffw
                    </div>
                </div>
                <div class="flex flex-row bg-black w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg">
                    <div class="w-[65%]">
                        <h4> Dates proches</h4>
                    </div>
                    <div class="bg-[#2176FF] w-[35%] rounded-r-lg">
                        ffw
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';

export default {
    name: 'dashboard',
    components: {
        sidebar,
    },
    created() {
        this.checkUserLoggedIn();
        console.log(localStorage.getItem('authToken'));
    },
    methods: {
        checkUserLoggedIn() {
            if (!localStorage.getItem('authToken')) {
                this.$router.push('/login');
            }
        }
    }
};
</script>


<style>

    h1 {
        color: black;
        font-size: 1.5rem;
    }

</style>