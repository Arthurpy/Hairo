<template>
  <div :class="{ 'light-theme': isLightMode, 'dark-theme': !isLightMode }" style="display: flex; justify-content: center;">
    <sidebar />
    <div class="main-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center;max-width: 800px; margin: auto;">
      <h1 class="mt-5" style="text-align: center;">Liste des événements</h1>
    <button class="my-button" @click="signInWithGoogle">Se connecter avec Google</button>
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
import axios from 'axios';
import sidebar from '../components/sidebar.vue';
export default {
  data() {
    return {
      events: [],
      isLightMode: true,
    };
  },
  mounted() {
    this.checkGoogleAuth();
    this.updateTheme();
  },
  components: {
    sidebar,
  },
  methods: {
    async checkGoogleAuth() {
      const jwt = localStorage.getItem('jwt');
      console.log('first jwt', jwt);
      if (!jwt) {
        await this.signInWithGoogle();
      }
      this.fetchEvents();
    },
    async signInWithGoogle() {
      try {
        const response = await axios.get('https://accounts.google.com/o/oauth2/auth', {
        params: {
          redirect_uri: 'http://localhost:5173/agenda/auth/google/callback',
          scope: 'https://www.googleapis.com/auth/calendar.readonly',
          response_type: 'code',
          client_id: '281350104013-egts6r5aqhpim3je7c3kdf6t1a04trah.apps.googleusercontent.com',
        }
    });
      const authorizationCode = response.data.code;
      const tokenResponse = await axios.post('https://oauth2.googleapis.com/token', {
      code: authorizationCode,
      client_id: '281350104013-egts6r5aqhpim3je7c3kdf6t1a04trah.apps.googleusercontent.com',
      client_secret: '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',
      redirect_uri: 'http://localhost:5173/agenda/auth/google/callback',
      grant_type: 'authorization_code',
      });
      const accessToken = tokenResponse.data.access_token;
      const calendarResponse = await axios.get('https://www.googleapis.com/calendar/v3/calendars/primary/events', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      });
      console.log('Événements du Google Calendar :', calendarResponse.data);
      } catch (error) {
        console.error('Erreur lors de la connexion à Google :', error);
      }
    },
    fetchEvents() {
      console.log('Récupération des événements...');
      const jwt = localStorage.getItem('jwt');
      console.log('jwt', jwt);
      axios.get('http://localhost:8000/api/events/', {
      headers: {
      'Authorization': `Bearer ${jwt}`
      }
      })
      .then(response => {
      console.log('Evénements récupérés :', response.data)
      this.events = response.data;
      })
      .catch(error => {
      console.error('Erreur lors de la récupération des événements :', error);
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
