<template>
    <div class="login_page">
        <div class="photo">
        <img  class="bateau" src="../assets/login.png">
        </div>
        <div2 class="infodiv">
            <logo/>
            <register_com/>
        </div2>
    </div>
</template>

<script>
    import logo from '../components/logo.vue'
    import register_com from '../components/register_com.vue';

    export default {
        name: 'Login',
        components: {
            logo,
            register_com,
        },
        data() {
            return {
                rememberMe: false,
            };
        },
    }
</script>

