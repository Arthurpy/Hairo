<template>
    <div class="sidebar">
      <logo />
      <div class="titre-sb">
        <RouterLink to="/dashboard">
          <button class="page" :class="{ active: activeButton === 'dashboard' }">
            <img class="icon" src="../assets/logo-home.png">
            Dashboard
          </button>
        </RouterLink>
        <RouterLink to="/dashboard">
          <button class="page" :class="{ active: activeButton === 'cas-pratiques' }">
            <img class="icon" src="../assets/cas_pratique_logo.png">
            Cas Pratiques
          </button>
        </RouterLink>
        <RouterLink to="/dashboard">
          <button class="page" :class="{ active: activeButton === 'ressource' }">
            <img class="icon" src="../assets/logo-ressources.png">
            ressource
          </button>
        </RouterLink>
      </div>
      <footer class="sett">
        <button class="page" :class="{ active: activeButton === 'settings' }">
          <img class="icon" src="../assets/logo-setting.png">
          Settings
        </button>
        <button class="page" :class="{ active: activeButton === 'logout' }">
          <img class="icon" src="../assets/logo-logout.png">
          Logout
        </button>
      </footer>
    </div>
  </template>

  <script>
  import { RouterLink } from 'vue-router';
import Poppins from '../assets/Poppins-Regular.ttf'
  import logo from './logo.vue'


  export default {
    name: 'Sidebar',
    components: {
    logo,
    RouterLink
},
    data() {
      return {
        activeButton: 'dashboard'
      };
    }
  }
  </script>

<style>

.titre_sb {
    display: flex;
    padding-left: 63px;
    flex-direction: column;
    align-items: center;
    align-self: stretch;
}

.sidebar {
    width: 275px;
    height: 100vh;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    padding-top: 50px;
    border-right: #001a452c;
    border-style: outset;
    align-items: center;
    background-color: #fff;
}

.icon {
    width: 24px;
    height: 24px;
    margin-right: 19px;
}

.page {
    color: #001A45;
    font-family: Poppins;
    font-size: 90%;
    font-style: normal;
    font-weight: 600;
    display: flex;
    padding-top: 10px;
    padding-bottom: 10px;
    width: 237px;
    padding-left: 20px;
}

.sett {
    margin-top: auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-bottom: 20px;
    flex-direction: column;
}

.page.active {
    border-radius: 4px;
    background: #D6EDFB;
    color: #2176FF;
    border-radius: 4px;;
}


</style>
```