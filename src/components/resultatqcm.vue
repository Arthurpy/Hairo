<template>
    <div class="qcm">
        <p class="name">quiz n'3 </p>
        <p class="score">{{ value }}%</p>
    </div>
</template>

<script>
export default {
    name: 'Resultatqcm',
    data() {
        return {
            value: 0,
        }
    },
    props: ['value'],
}
</script>

<style>

.qcm {
    width: 133px;
    height: 124px;
    border-radius: 10px;
    flex-shrink: 0;
    background-color: #B4E1FE;
}

.name {
    height: 23px;
    flex-shrink: 0;
    color: #252525;
    font-family: Poppins;
    font-size: 10px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    opacity: 0.72;
    padding-top: 17px;
    padding-left: 20px;
}

.score {
    width: 80px;
    height: 80px;
    flex-shrink: 0;
    color: #252525;
    font-family: Poppins;
    font-size: 32px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    display: flex;
    align-items: flex-end;
    padding-left: 14px;
}


</style>