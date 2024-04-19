<template>
  <div :class="{ 'light-theme': isLightMode, 'dark-theme': !isLightMode }" style="display: flex;">
    <sidebar />
    <div class="main-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center; max-width: 800px; margin: auto;">
      <h1 class="mt-5" style="text-align: center;">Liste des événements</h1>
      <button v-if="!microsoftToken" @click="openMicrosoftLogin">Se connecter avec Microsoft</button>
      <p v-else class="mt-5" style="text-align: center;">Bienvenue, utilisateur Microsoft!</p>
      <ul v-if="events.length">
        <li v-for="event in events" :key="event.id">{{ event.subject }}</li>
      </ul>
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
    const urlParams = new URLSearchParams(window.location.search);
    const accessToken = urlParams.get('access_token');
    if (accessToken) {
      localStorage.setItem('microsoft_access_token', accessToken);
      window.history.pushState({}, document.title, "/");
      this.fetchCalendarData();
    }
    this.updateTheme();
  },
  components: {
    sidebar,
  },
  methods: {
    openMicrosoftLogin() {
      window.location.href = 'http://localhost:8000/microsoft-login/';
    },
    redirectToDashboard() {
      this.$router.push('/dashboard');
    },
    updateTheme() {
      if (this.isLightMode) {
        document.documentElement.style.backgroundColor = '#ffffff';
        document.documentElement.style.color = '#000000';
      } else {
        document.documentElement.style.backgroundColor = '#000000';
        document.documentElement.style.color = '#ffffff';
      }
    },
    fetchCalendarData() {
      const headers = new Headers({
        'Authorization': `Bearer ${localStorage.getItem('microsoft_access_token')}`,
        'Content-Type': 'application/json'
      });
      const url = 'https://graph.microsoft.com/v1.0/me/calendars';
      fetch(url, { headers })
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to fetch calendar data');
          }
        })
        .then(data => {
          this.events = data.value;
          console.log('Calendar Data: ++++++++++++++++++++++++++++++++++++++++++++++++++++', this.events);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
    data() {
        return {
          events: [],
        }
      }
  }
};
</script>

<style scoped>
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
