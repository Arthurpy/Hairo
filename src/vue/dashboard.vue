<template>
  <sidebar :active-button="'settings'"/>
  <div class="settings-page" style="background: white; height: 100vh;">
    <h1>Paramètres</h1>
    <section class="language-settings">
      <h2>Paramètres de langue</h2>
      <div>
        <label for="language">Langue :</label>
        <select v-model="selectedLanguage" id="language">
          <option value="fr">Français</option>
        </select>
      </div>
    </section>
    
    <section class="profile-settings">
      <h2>Informations du profil</h2>
      <div>
        <label for="name">Nom :</label>
        <input type="text" id="name" v-model="profile.name" />
      </div>
      <div>
        <label for="email">prenom :</label>
        <input type="email" id="prenom" v-model="profile.prenom" />
      </div>
      <div>
        <label for="email">faculté :</label>
        <input type="email" id="faculté" v-model="profile.faculté" />
      </div>
      <div>
        <label for="email">Tutorat :</label>
        <input type="email" id="Tutorat" v-model="profile.Tutorat" />
      </div>
      <div>
        <label for="email">Moyenne Visée :</label>
        <input type="email" id="Moyenne_Visée" v-model="profile.Moyenne_Visée" />
      </div>
      <div>
        <label for="bio">Lieux d'études :</label>
        <textarea id="bio" v-model="profile.bio"></textarea>
      </div>
    </section>
    
    <button @click="saveSettings">Sauvegarder les paramètres</button>
    <div>
      <a href="/path/to/conditions_ventes.pdf" target="_blank">Conditions générales de ventes et d'utilisation</a>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';

export default {
  data() {
    return {
      selectedLanguage: 'fr',
      profile: {
        name: '',
        email: '',
        bio: ''
      }
    };
  },
  components: {
    sidebar
  },
  methods: {
    saveSettings() {
      // Logic to save settings goes here
      console.log('Paramètres sauvegardés:', {
      language: this.selectedLanguage,
      profile: this.profile
      });
      alert('Paramètres sauvegardés avec succès !');

      // Send data to backend
      fetch('/api/saveSettings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        language: this.selectedLanguage,
        profile: this.profile
      })
      })
      .then(response => response.json())
      .then(data => {
      console.log('Response from backend:', data);
      })
      .catch(error => {
      console.error('Error saving settings:', error);
      });
    }
  }
};
</script>

<style scoped>
.settings-page {
  margin: 0 auto;
  padding: 20px;
  margin-left: 18rem;
}

.settings-page h1, .settings-page h2 {
  text-align: center;
}

.settings-page label {
  display: block;
  margin-top: 10px;
}

.settings-page input, .settings-page select, .settings-page textarea {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
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
}

.settings-page button:hover {
  background-color: #0056b3;
}
</style>
