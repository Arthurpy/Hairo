<template>
    <div class="flex flex-col items-center mt-10 bg-[#B4E1FE] rounded-tr-full">
        <h1 class="font-extrabold text-7xl lg:text-5xl mt-10">What We do</h1>
        <h1 class="text-7xl lg:text-5xl">For Your Revision</h1>
        <div class="my-20 flex flex-row ml-10 overflow-hidden">
            <Card title="Tu cherches une solution efficace pour la correction automatique des cas pratiques ? " value="Découvrez notre service unique : correction rapide et précise, retours personnalisés pour chaque étudiant. Grâce à l'intelligence artificielle, nous adaptons l'apprentissage à chaque besoin, offrant une expérience sur mesure et flexible." />
            <Card title="Nous te permettons de t'exercer à tout moments" value="Grâce à notre proposition de cas pratiques et de QCM accessibles à tous et à n'importe quel moment pour des révisions efficaces et adaptées et corriger en direct par notre Ia entrainer sur des cours de plus de 10 facultes sur 10ans d'anal." />
            <Card title="Tu veux de l'aide pour mieux t'organiser dans t'es revision" value="Nous te proposons de mieux t'organiser grâce a notre IA qui te permettra d'organiser ton planning avec nos suggestion en fonction de t'es résultat et de t'es besoins avec la méthode d'organisaton de notre IA" />
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