<template>
    <div class="sidebar bg-white w-58 fixed flex">
      <logo />
      <div class="titre-sb">
        <RouterLink to="/revisions">
          <button class="page btn-hover first-button" :class="{ active: activeButton === 'revisions' }">
            <img class="icon" src="../assets/Revision.png">
            Révision
          </button>
        </RouterLink>
        <RouterLink to="/ressources">
          <button class="page btn-hover" :class="{ active: activeButton === 'ressources' }">
            <img class="icon" src="../assets/Ressources.png">
            Ressource
          </button>
        </RouterLink>
        <RouterLink to="/dashboard">
          <button class="page btn-hover" :class="{ active: activeButton === 'dashboard' }">
            <img class="icon" src="../assets/Dashboard.png">
            Dashboard
          </button>
        </RouterLink>
        <RouterLink to="/agenda">
          <button class="page btn-hover" :class="{ active: activeButton === 'agenda' }">
            <img class="icon" src="../assets/Agenda.png">
            Agenda
          </button>
        </RouterLink>
        <RouterLink to="/messagerie">
          <button class="page btn-hover" :class="{ active: activeButton === 'messagerie' }">
            <img class="icon" src="../assets/Messagerie.png">
            Messagerie
          </button>
        </RouterLink>
        <RouterLink to="/notes">
          <button class="page btn-hover" :class="{ active: activeButton === 'notes' }">
            <img class="icon" src="../assets/Revision.png">
            Prise de notes
          </button>
        </RouterLink>
      </div>
      <footer class="sett">
      <RouterLink to="/settings">
        <button class="page btn-hover" :class="{ active: activeButton === 'settings' }">
          <img class="icon" src="../assets/logo-setting.png">
          Paramètres
        </button>
      </RouterLink>
        <button class="page btn-hover" :class="{ active: activeButton === 'logout'}" @click="logout" >
          <img class="icon" src="../assets/logo-logout.png">
          Logout
        </button>
      </footer>
    </div>
  </template>

  <script>
  import { RouterLink } from 'vue-router';
  import Poppins from './../assets/Poppins-Regular.ttf'
  import logo from './logo.vue'


  export default {
    name: 'Sidebar',
      components: {
      logo,
      RouterLink
    },
    props: {
      activeButton: {
        type: String,
      }
    },
    data() {
      return {
      };
    },
    methods: {
      logout() {
        localStorage.removeItem('authToken');
        this.$router.push('/login');
        console.log('logout');
      }
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
    font-family: ;
}

.sidebar {
    width: 25vw;
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
    background: #D2E3FF;
    color: black;
    border-radius: 5px;;
}

.btn-hover:hover {
    background-color: #FFA93E;
    border-radius: 5px;
    color: white;
}

.first-button {
  margin-top: 30px
}

.sidebar {
  position: ;
}

</style>
```