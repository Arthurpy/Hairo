<template>
  <div>
    <sidebar :active-button="'agenda'"/>
    <div class="bg-blue-200" style="margin-left: 18rem; display: flex; flex-direction: column; align-items: center;">
      <div class="flex flex-col">
        <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] rounded-lg justify-between items-center mt-10 py-16">
          <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Agenda</h1>
        </div>
      </div>
      <div class="main-content h-screen" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div class="carousel-container">
          <button @click="prevMonth" class="carousel-button">‹</button>
          <div class="calendars-wrapper">
            <vue-cal
              v-for="index in 1"
              :key="index"
              :default-view="'month'"
              :time="getMonthTime(index)"
              :events="events"
              :locales="locales"
              :locale="'fr'"
              style="height: 500px; width: 400px; margin: 0 10px; background-color: white; border-radius: 10px; padding: 20px; color: black; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"
              class="custom-vuecal"
            ></vue-cal>
          </div>
          <button @click="nextMonth" class="carousel-button">›</button>
        </div>
        <div class="event-list">
          <h2>Upcoming Events</h2>
          <div class="events-container">
            <ul>
              <li v-for="event in sortedEvents" :key="event.id">
                {{ event.title }} - {{ new Date(event.start).toLocaleDateString('fr-FR') }}
              </li>
            </ul>
          </div>
        </div>
        <div class="revision-planner">
          <h2>Planificateur de Révision</h2>
          <form @submit.prevent="generateRevisionPlan">
            <label for="weekly-hours">Heures de révision hebdomadaires:</label>
            <input type="number" id="weekly-hours" v-model="weeklyHours" required>

            <label for="session-length">Durée de chaque session (en minutes):</label>
            <input type="number" id="session-length" v-model="sessionLength" required>

            <button type="submit">Générer le planning</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';

const fr = {
  weekDays: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
  months: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
  years: 'Années',
  year: 'An',
  month: 'Mois',
  week: 'Semaine',
  day: 'Jour',
  today: "Aujourd'hui",
  noEvent: 'Aucun événement',
  allDay: 'Toute la journée',
  deleteEvent: 'Supprimer',
  createEvent: 'Créer un événement',
  dateFormat: 'dddd D MMMM YYYY',
  timeFormat: 'HH:mm',
  eventModalSave: 'Sauvegarder',
  eventModalClose: 'Fermer',
  eventModalDelete: 'Supprimer',
};

export default {
  data() {
    return {
      events: [],
      currentMonth: new Date(),
      accessToken: null,
      weeklyHours: 0,
      sessionLength: 0,
      locales: {
        'fr': fr
      }
    };
  },
  mounted() {
    this.accessToken = localStorage.getItem('microsoft_access_token');
    if (!this.accessToken) {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.has('access_token')) {
        this.accessToken = urlParams.get('access_token');
        localStorage.setItem('microsoft_access_token', this.accessToken);
        window.history.pushState({}, document.title, "/");
      } else {
        this.openMicrosoftLogin();
        return;
      }
    }
    this.fetchCalendarData();
  },
  components: {
    sidebar,
    VueCal,
  },
  computed: {
    sortedEvents() {
      const today = new Date();
      const twoMonthsLater = new Date();
      twoMonthsLater.setMonth(today.getMonth() + 2);

      return this.events
        .filter(event => new Date(event.start) >= today && new Date(event.start) <= twoMonthsLater)
        .sort((a, b) => new Date(a.start) - new Date(b.start));
    }
  },
  methods: {
    openMicrosoftLogin() {
      window.location.href = 'http://localhost:8000/microsoft-login/';
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
          if (data.value === undefined) {
            this.accessToken = null;
            localStorage.removeItem('microsoft_access_token');
            this.refreshPage();
            return;
          }
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
                  id: event.id,
                  start: new Date(event.start.dateTime),
                  end: new Date(event.end.dateTime),
                  title: event.subject,
                  body: event.bodyPreview,
                  class: 'microsoft-event',
                  background: true,
                };
              }
            }).filter(Boolean)
          );
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
    prevMonth() {
      const newTime = new Date(this.currentMonth);
      newTime.setMonth(newTime.getMonth() - 1);
      this.currentMonth = newTime;
    },
    nextMonth() {
      const newTime = new Date(this.currentMonth);
      newTime.setMonth(newTime.getMonth() + 1);
      this.currentMonth = newTime;
    },
    getMonthTime(index) {
      const newDate = new Date(this.currentMonth);
      newDate.setMonth(newDate.getMonth() + (index - 2));
      return newDate;
    },
    refreshPage() {
      window.location.reload();
    },
    async generateRevisionPlan() {
      try {
        const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ailQ8oCys1xqRhIClx4ET3BlbkFJwDXtUdP4wGEaQhRgCkdY`
          },
          body: JSON.stringify({
            prompt: `Plan a study schedule with the following criteria: Weekly study hours: ${this.weeklyHours}, Session length in minutes: ${this.sessionLength}, using the spaced repetition method.`,
            max_tokens: 150
          })
        });
        const data = await response.json();
        const schedule = JSON.parse(data.choices[0].text);
        this.events.push(...schedule);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  },
};
</script>

<style scoped>
.carousel-container {
  display: flex;
  align-items: center;
}

.calendars-wrapper {
  display: flex;
  justify-content: center;
  width: 1200px;
  overflow: hidden;
}

.carousel-button {
  background: none;
  border: none;
  font-size: 2em;
  cursor: pointer;
}

.event-list {
  margin-top: 20px;
  width: 80%;
  text-align: center;
}

.event-list h2 {
  font-size: 2em;
  margin-bottom: 10px;
  color: black;
}

.events-container {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.event-list ul {
  list-style: none;
  padding: 0;
}

.event-list li {
  background: none;
  margin: 5px 0;
  padding: 10px;
}

.custom-vuecal {
  --vuecal-primary: #2176FF; /* Change primary color */
  --vuecal-text-color: #000000; /* Change text color */
  --vuecal-border-color: #ddd; /* Change border color */
  --vuecal-today-bg: #e6f0ff; /* Change today's background color */
  --vuecal-weekday-bg: white; /* Change weekday background color */
}

.revision-planner {
  margin-top: 20px;
  width: 80%;
  text-align: center;
}

.revision-planner h2 {
  font-size: 2em;
  margin-bottom: 10px;
  color: black;
}

.revision-planner form {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.revision-planner label {
  display: block;
  margin-bottom: 5px;
  color: black;
}

.revision-planner input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background: white;
  color: black;
  border: 1px black solid;
  border-radius: 20px;
}

.revision-planner button {
  background-color: #2176FF;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.revision-planner button:hover {
  background-color: #0056b3;
}
</style>
