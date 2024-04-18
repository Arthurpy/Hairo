<template>
  <div :class="{ 'light-theme': isLightMode, 'dark-theme': !isLightMode }" style="display: flex;">
    <sidebar />
    <div class="main-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center;max-width: 800px; margin: auto;">
      <h1 class="mt-5" style="text-align: center;">Liste des événements</h1>
    <ul>
      <li v-for="event in events" :key="event.id" >{{ event.title }}</li>
    </ul>
    <div v-for="event in events" :key="event.id">
      <h2>{{ event.title }}</h2>
      <p>{{ event.date }}</p>
      <p>{{ event.description }}</p>
    </div>
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
    if (!microsoftToken) {
      this.openMicrosoftLogin();
    } else {
      this.checkMicrosoftValidity(microsoftToken);
    }
    this.updateTheme();
  },
  components: {
    sidebar,
  },
  methods: {
    openMicrosoftLogin() {
      window.open('http://login.microsoftonline.com/common/oauth2/v2.0/authorize', '_self');
    },
    checkMicrosoftValidity(token) {
      fetch('http://localhost:8000/auth/microsoft/validity', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.valid) {
            localStorage.setItem('microsoftToken', token);
            this.$router.push('/ressources');
          } else {
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
