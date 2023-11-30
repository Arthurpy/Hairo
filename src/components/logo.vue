<template>
    <div>
    <img src="../assets/logo.png" alt="logo" class="logo">
    <p class="title">AIRO</p>
    </div>
</template>

<script>

import Poppins from '../assets/Poppins-Regular.ttf'
export default {
    name: 'Logo',
}

</script>

<style scoped>

div {
    max-width: fit-content;
    display: flex;
    align-items: baseline;
    margin-bottom: 20px;
}

.logo {
    width: 44.1px;
    height: 42px;
    margin: 0 auto;
    margin-left: 20px;
}

.title {
    color: #2176FF;
    text-align: center;
    font-family: Inter;
    font-size: 28.998px;
    font-style:normal;
    font-weight: 800;
    line-height: normal;
}

</style>