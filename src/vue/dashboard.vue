<template>
    <div class="bg-[#F4FBFF] flex">
        <sidebar :activeButton="'dashboard'"/>
        <div class="flex flex-col ml-80 h-screen">
            <div class="flex mt-[40px] bg-black w-[70vw] h-[56px] ml-[50px] rounded-lg">
                <h4> Dashboard </h4>
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
                <div class="flex flex-col bg-black w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg">
                    <div class="h-[70%]">
                        <h4> Dates proches</h4>
                    </div>
                    <div class="bg-[#2176FF] h-[30%] rounded-b-lg">
                        ffw
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