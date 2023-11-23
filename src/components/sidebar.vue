<template>
    <div class="sidebar">
        <logo/>
        <div1 class="titre">
        <button class="page">
            <img class="icon" src="..//assets/logo-home.png">
            Dashboard</button>
        <button class="page">
            <img class="icon" src="..//assets/logo-ressources.png">
            Ressources
        </button>
        <button class="page">
            <img class="icon" src="..//assets/cas_pratique_logo.png">
            Cas Pratiques
        </button>
        </div1>
        <footer class="sett">
            <button class="page">
                <img class="icon" src="..//assets/logo-setting.png">
                Settings
            </button>
            <button class="page">
                <img class="icon" src="..//assets/logo-logout.png">
                Logout
            </button>
        </footer>
    </div>

</template>


<script>
import Poppins from '..//assets/Poppins-Regular.ttf'
import logo from './logo.vue'

export default {
  name: 'Sidebar',
  components: {
    logo
  },

}

</script>


<style>

.titre {
    display: table-column-group;
    margin-top: 20px;
    width: fit-content;
    margin-left: -80px;
}

.sidebar {
    width: 275px;
    height: 100vh;
    flex-shrink: 0;
    background: #FFF;
    display: flex;
    flex-direction: column;
    padding: 50px;
}

.icon {
    width: 24px;
    height: 24px;
    margin-right: 19px;
}

.page {
    color: #001A45;
    font-family: Poppins;
    font-size: 16px;
    font-style: normal;
    font-weight: 600;
    line-height: 19.104px;
    display: flex;
    padding: 20px;
    align-items: center;
}

.sett {
    margin-top: auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-bottom: 20px;
    flex-direction: column;
}

</style>
```