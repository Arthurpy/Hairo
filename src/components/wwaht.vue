<template>
    <div class="flex flex-col items-center mt-10 bg-[#B4E1FE] rounded-tr-full">
        <h1 class="font-extrabold text-4xl lg:text-7xl mt-10"> Qu’est-ce que Hairo ? </h1>
        <!-- <h1 class="text-4xl lg:text-7xl ">Pour tes révisions ?</h1> -->
        <div class="my-20 flex lg:flex-row flex-col verflow-hidden justify-center">
            <Card title="Tu galères à réviser et à t'organiser ? " value="Hairo propose un calendrier intelligent qui te permet de gérer ton temps et de t’organiser en fonction de ton style de travail, de ta charge de travail et de tes échéances. Il est capable de te proposer des plannings de révisions en utilisant les méthodes de ton choix approuvées par d'anciens étudiants." />
            <Card title="Tu n’arrives pas à être efficient dans tes révisions ?" value="Grâce à Hairo et aux ressources de ton tutorat, tu peux accéder à une large bibliothèque de ressources. Tu peux les consulter quand tu le souhaites et où tu le souhaites. Hairo te propose des QCM type examen à partir de ces cours, grâce à l’IA, pour t’entraîner." />
            <Card title="Le rythme est trop dur à suivre, où tu en es ?" value="Hairo est l’outil qui te permet de t’exercer, de t’organiser, mais aussi de bien ranger ta prise de notes ainsi que d’être en contact continu avec le tutorat. On te propose aussi des visuels sur ta progression, pour cibler tes lacunes et t’accompagner vers la réussite." />
        </div>
    </div>
</template>

<script>
import Card from './mycard.vue';

export default {
    name: 'What',
    components: { Card }
}
</script>