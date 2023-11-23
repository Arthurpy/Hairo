<template>
    <div>
    <img src="..//assets/logo.png" alt="logo" class="logo">
    <p class="title">AIRO</p>
    </div>
</template>

<script>

import Poppins from '..//assets/Poppins-Regular.ttf'
export default {
    name: 'Logo',
}

</script>

<style scoped>

div {
    max-width: fit-content;
    display: flex;
    align-items: baseline;
}

.logo {
    width: 100px;
    height: 100px;
    margin: 0 auto;
}

.title {
    font-size: 30px;
    font-weight: bold;
    color: #2176FF;
    font-family: 'Poppins', sans-serif;
}

</style>