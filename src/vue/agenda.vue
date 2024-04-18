<template>
  <div :class="{ 'light-theme': isLightMode, 'dark-theme': !isLightMode }" style="display: flex;">
    <sidebar />
    <div class="main-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center;max-width: 800px; margin: auto;">
    <h1 class="mt-5" style="text-align: center;">Liste des événements</h1>
    <button v-if="!microsoftToken" @click="openMicrosoftLogin">Se connecter avec Microsoft</button>
      <p v-else class="mt-5" style="text-align: center;">Bienvenue, utilisateur Microsoft!</p>
    <button class="my-button" @click="redirectToDashboard">Retour au Dashboard</button>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
export default {
  data() {
    return {
      events: [],
      isLightMode: true,
    };
  },
  mounted() {
    const microsoftToken = localStorage.getItem('microsoftToken');
    if (microsoftToken) {
      this.checkMicrosoftValidity(microsoftToken);
    }
    this.updateTheme();
  },
  components: {
    sidebar,
  },
  methods: {
    openMicrosoftLogin() {
      fetch('http://localhost:8000/auth/microsoft/login', {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data.url) {
            window.open(data.url, '_self');
          }
        });
    },
    checkMicrosoftValidity(token) {
      console.log('Checking Microsoft token validity');
      fetch('http://localhost:8000/auth/microsoft/callback', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data.valid) {
            localStorage.setItem('microsoftToken', token);
            this.microsoftToken = token;
            this.$router.push('/ressources');
          } else {
            this.microsoftToken = null;
            this.openMicrosoftLogin();
          }
        });
    },
    redirectToDashboard() {
      // Rediriger vers le Dashboard (à adapter selon ton chemin d'accès)
      this.$router.push('/dashboard');
    },
    updateTheme() {
      if (this.isLightMode) {
        document.documentElement.style.backgroundColor = '#ffffff'; // Fond blanc
        document.documentElement.style.color = '#000000'; // Texte noir
      } else {
        document.documentElement.style.backgroundColor = '#000000'; // Fond noir
        document.documentElement.style.color = '#ffffff'; // Texte blanc
      }
    }
  }
};
</script>

<style scoped>
/* Ajoute du style CSS au besoin */
.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.light-theme {
  background-color: #ffffff;
  color: #000000;
}

.dark-theme {
  background-color: #000000;
  color: #ffffff;
}

.my-button {
  background-color: blue;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.my-button:hover {
  background-color: rgba(255, 208, 0, 0.603);
}
</style>
