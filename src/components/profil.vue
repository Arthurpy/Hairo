<template>
    <div class="w-[22vw] h-screen bg-white flex flex-col items-center justify-center">
        <div class="avatar avatar-ring-primary avatar-xl w-4/5 h-40 flex-shrink-0 rounded-full border-4 border-[#FCD19C]">
	        <img src="https://i.pravatar.cc/150?u=a042581f4e29026024d" alt="avatar" />
        </div>
        <p class=""> Arthur Kealtes </p>
        <p> 1 ère année <br> </p>
        <p> Calendar</p>
    </div>

</template>

<script>

export default {
  name: 'profil',
  data() {
    return {
    }
  },
}

</script>

<style>

p {
  color: black;
  font-size: 1.5rem;
}

.profil {
    width: 225px;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

</style>