<template>
  <div :class="{ 'light-theme': isLightMode, 'dark-theme': !isLightMode }" style="display: flex;">
    <sidebar />
    <div class="main-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center; max-width: 800px; margin: auto; gap: 80px;">
      <button @click="openMicrosoftLogin">Se connecter avec Microsoft</button>
      <vue-cal :events="events" style="height: 600px; width: 1200px;" class="vuecal--blue-theme"></vue-cal>
      <button class="my-button" @click="redirectToDashboard">Retour au Dashboard</button>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';
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
    this.events.push();
  },
  components: {
    sidebar,
    VueCal,
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
        .then(response => response.json())
        .then(data => {
          const calendarPromises = data.value.map(calendar => {
          const eventsUrl = `https://graph.microsoft.com/v1.0/me/calendars/${calendar.id}/events`;
          return fetch(eventsUrl, { headers }).then(response => response.json());
        });
        return Promise.all(calendarPromises);
      })
        .then(calendarsData => {
      this.events = calendarsData.flatMap(data =>
        data.value.map(event => {
          if (event.start && event.end) {
            return {
              start: new Date(event.start.dateTime),
              end: new Date(event.end.dateTime),
              title: event.subject,
              body: event.bodyPreview,
              class: 'microsoft-event',
            };
          }
        }).filter(Boolean)
      );
      console.log('All Events:', this.events);
    })
        .catch(error => {
          console.error('Error:', error);
        });
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

.vuecal__event {
  border-radius: 4px;
  padding: 4px;
}
.vuecal__event.microsoft-event {
  background-color: #0078d4;
  color: white;
}
</style>
