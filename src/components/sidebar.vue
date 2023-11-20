<template>
    <div class="sidebar">
      <logo />
      <div class="titre-sb">
        <button class="page" :class="{ active: activeButton === 'dashboard' }">
          <img class="icon" src="../assets/logo-home.png">
          Dashboard
        </button>
        <button class="page" :class="{ active: activeButton === 'ressources' }">
          <img class="icon" src="../assets/logo-ressources.png">
          Ressources
        </button>
        <button class="page" :class="{ active: activeButton === 'cas-pratiques' }">
          <img class="icon" src="../assets/cas_pratique_logo.png">
          Cas Pratiques
        </button>
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
  import Poppins from '../assets/Poppins-Regular.ttf'
  import logo from './logo.vue'

  export default {
    name: 'Sidebar',
    components: {
      logo
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
    border-right: #001A45;
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