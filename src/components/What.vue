<template>
    <div class="flex flex-col items-center mt-10 bg-[#B4E1FE] rounded-tr-full">
        <h1 class="font-extrabold text-7xl lg:text-5xl mt-10">What We do</h1>
        <h1 class="text-7xl lg:text-5xl">For Your Revision</h1>
        <div class="my-20 flex flex-row ml-10 overflow-hidden">
            <Card/>
            <Card/>
        </div>
    </div>
</template>

<script>
import Card from './Card.vue';

export default {
    name: 'What',
    components: { Card }
}
</script>