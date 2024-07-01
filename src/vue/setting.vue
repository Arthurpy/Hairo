<template>
    <sidebar :active-button="'settings'"/>
    <div class="settings-page bg-blue-200" style="height: 100%;">
      <div class="flex bg-white text-[#2176FF] h-[56px] rounded-lg justify-between items-cente py-16 mb-10">
        <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Paramètres</h1>
      </div>
      <section class="language-settings">
        <h1 style="font-size: large; font-weight: 700;">Paramètres de langue</h1>
        <div style="display: flex; justify-content: space-evenly">
          <div style="display: flex; flex-direction: column; width: 30%;">
            <label for="language">Langue :</label>
            <select v-model="selectedLanguage" id="language">
              <option value="fr">Français</option>
            </select>
          </div>
          <div style="display: flex; flex-direction: column; width: 30%;">
            <label for="mode">Mode :</label>
            <select v-model="selectedMod" id="mode">
              <option value="lg">Light Mode</option>
            </select>
          </div>
        </div>
      </section>
  
      <section class="profile-settings">
        <h2 style="padding-top: 20px; font-size: large; font-weight: 700">Informations du profil </h2>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="name">Nom :</label>
          <input type="text" id="name" v-model="profile.name" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="prenom">Prénom :</label>
          <input type="text" id="prenom" v-model="profile.prenom" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="faculte">Faculté :</label>
          <input type="text" id="faculte" v-model="profile.faculte" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="tutorat">Tutorat :</label>
          <input type="text" id="tutorat" v-model="profile.tutorat" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="moyenne_visee">Moyenne Visée :</label>
          <input type="text" id="moyenne_visee" v-model="profile.moyenne_visee" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="rank">Rang :</label>
          <input type="text" id="rank" v-model="profile.rank" />
        </div>
        <div style="display: flex; flex-direction: column; width: 100%; align-items: center;">
          <label for="rank">Picture :</label>
            <input type="file" id="rank" v-on="profile.picture" />
        </div>
      </section>
      <button @click="saveSettings">Sauvegarder les paramètres</button>
      <div class="m-10; flex" style="display: flex; justify-content: center; padding-top: 10px;">
        <a style="color: blue;" href="src/assets/CGU-CGV.pdf" target="_blank">Conditions générales de ventes et d'utilisation</a>
      </div>
    </div>
  </template>
  
  <script>
  import sidebar from '../components/sidebar.vue';
  
  export default {
    name: 'settings',
    data() {
      return {
        selectedLanguage: 'fr',
        selectedMod: 'lg',
        profile: {
          name: '',
          prenom: '',
          faculte: '',
          tutorat: '',
          moyenne_visee: '',
          rank: '',
        }
      };
    },
    components: {
      sidebar
    },
    mounted() {
      this.loadSettings();
    },
    methods: {
      async loadSettings() {
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('No token found in localStorage');
          return;
        }
  
        try {
          const response = await fetch('http://localhost:8000/api/loadSettings', {
            method: 'GET',
            headers: {
              'Authorization': `Bearer ${token}`
            },
            credentials: 'include'
          });
          if (response.ok) {
            const data = await response.json();
            this.profile = data.profile;
          } else {
            console.error('Failed to load settings');
          }
        } catch (error) {
          console.error('Error loading settings:', error);
        }
      },
      async saveSettings() {
        const settingsData = {
          language: this.selectedLanguage,
          mode: this.selectedMod,
          profile: this.profile
        };
  
        const token = localStorage.getItem('authToken');
        if (!token) {
          console.error('No token found in localStorage');
          return;
        }
  
        try {
          const response = await fetch('http://localhost:8000/api/saveSettings', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`,
              'X-CSRFToken': this.getCookie('csrftoken')
            },
            body: JSON.stringify(settingsData),
            credentials: 'include'
          });
          if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(errorMessage);
          }
          const data = await response.json();
          console.log('Response from backend:', data);
        } catch (error) {
          console.error('Error saving settings:', error);
        }
      },
      getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
    }
  };
  </script>
  
  <style scoped>
    .settings-page {
      margin: 0 auto;
      padding: 100px;
      margin-left: 18rem;
      color: black;
    }
  
    .settings-page h1, .settings-page h2 {
      text-align: center;
    }
  
    .settings-page label {
      display: block;
      margin-top: 10px;
      padding-left: 15px;
    }
  
    .settings-page input, .settings-page select, .settings-page textarea {
      width: 80%;
      padding: 8px;
      margin-top: 5px;
      background: white;
      border: 1px solid rgba(0, 0, 0, 0.538);
      border-radius: 50px;
    }
  
    .settings-page button {
      display: block;
      width: 100%;
      padding: 10px;
      margin-top: 20px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      cursor: pointer;
      border-radius: 20px;
    }
  
    .settings-page button:hover {
      background-color: #0056b3;
      border-radius: 20px;
    }
  </style>
  