<template>
  <div>
    <sidebar :active-button="'agenda'"/>
    <div class="bg-blue-200" style="margin-left: 18rem; display: flex; flex-direction: column; align-items: center;">
      <div class="flex flex-col">
        <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] rounded-lg justify-between items-center mt-10 py-16">
          <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Agenda</h1>
          <button @click="logout" class="bg-red-500 text-white py-2 px-4 rounded-lg mr-10">Déconnexion</button>
        </div>
      </div>
      <div class="main-content p-8" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div class="carousel-container">
          <div class="calendars-wrapper">
            <vue-cal
              v-for="index in 1"
              :key="index"
              :default-view="'month'"
              :time="getMonthTime(index)"
              :events="events"
              :locales="locales"
              :locale="'fr'"
              :editable="true"
              @event-change="onEventChange"
              style="height: 500px; width: 400px; margin: 0 10px; background-color: white; border-radius: 10px; padding: 20px; color: black; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"
              class="custom-vuecal"
            ></vue-cal>
          </div>
        </div>
        <div class="event-list">
          <h2>Evenement à venir</h2>
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
        <!-- Nouveau formulaire pour ajouter des événements -->
        <div class="add-event">
          <h2>Ajouter un événement</h2>
          <form @submit.prevent="addEvent">
            <label for="event-title">Titre de l'événement:</label>
            <input type="text" id="event-title" v-model="newEvent.title" required>
            <div style="display: flex; justify-content: space-evenly; align-items: center;">
              <div>
                <label for="event-start">Date de début:</label>
                <input type="datetime-local" id="event-start" v-model="newEvent.start" required>
              </div>
              <div style="display: flex; flex-direction: column;">
                <label for="event-end">Date de fin:</label>
                <input type="datetime-local" id="event-end" v-model="newEvent.end" required>
              </div>
              <div style="display: flex; flex-direction: row;">
                <label for="event-color">Couleur de l'événement:</label>
                <input type="color" id="event-color" v-model="newEvent.color" style="width: 5%; height: 5%; border-radius: 6px; margin-left: 5px;" required>
              </div>
            </div>
            <button type="submit">Ajouter l'événement</button>
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
      newEvent: {
        title: '',
        start: '',
        end: '',
        color: '#2176FF' // Couleur par défaut
      },
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
                  color: event.color ? event.color : '#2176FF' // Assurez-vous d'inclure une couleur par défaut
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
    },
    async addEvent() {
      const newEvent = {
        subject: this.newEvent.title,
        start: {
          dateTime: new Date(this.newEvent.start).toISOString(),
          timeZone: 'UTC'
        },
        end: {
          dateTime: new Date(this.newEvent.end).toISOString(),
          timeZone: 'UTC'
        },
        body: {
          contentType: 'HTML',
          content: ''
        },
        color: this.newEvent.color // Ajouter la couleur de l'événement
      };

      try {
        const headers = new Headers({
          'Authorization': `Bearer ${localStorage.getItem('microsoft_access_token')}`,
          'Content-Type': 'application/json'
        });
        const url = 'https://graph.microsoft.com/v1.0/me/events';
        const response = await fetch(url, {
          method: 'POST',
          headers,
          body: JSON.stringify(newEvent)
        });
        const data = await response.json();

        this.events.push({
          id: data.id,
          start: new Date(this.newEvent.start),
          end: new Date(this.newEvent.end),
          title: this.newEvent.title,
          color: this.newEvent.color,
          class: 'custom-event',
          background: true,
        });

        // Réinitialiser le formulaire après l'ajout
        this.newEvent = {
          title: '',
          start: '',
          end: '',
          color: '#2176FF' // Réinitialiser la couleur à la valeur par défaut
        };
      } catch (error) {
        console.error('Error adding event:', error);
      }
    },
    onEventChange({ event, newStart, newEnd }) {
      const updatedEvent = this.events.find(e => e.id === event.id);
      if (updatedEvent) {
        updatedEvent.start = newStart;
        updatedEvent.end = newEnd;
        // Sauvegarder les modifications sur le backend (Microsoft Calendar API)
        this.updateEventOnServer(updatedEvent);
      }
    },
    updateEventOnServer(event) {
      const headers = new Headers({
        'Authorization': `Bearer ${localStorage.getItem('microsoft_access_token')}`,
        'Content-Type': 'application/json'
      });
      const url = `https://graph.microsoft.com/v1.0/me/events/${event.id}`;
      fetch(url, {
        method: 'PATCH',
        headers,
        body: JSON.stringify({
          start: {
            dateTime: event.start.toISOString(),
            timeZone: 'UTC'
          },
          end: {
            dateTime: event.end.toISOString(),
            timeZone: 'UTC'
          },
          subject: event.title,
          body: {
            contentType: 'HTML',
            content: event.body || ''
          },
          color: event.color // Assurez-vous que la couleur est incluse dans la mise à jour
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Event updated on server:', data);
      })
      .catch(error => {
        console.error('Error updating event on server:', error);
      });
    },
    logout() {
      localStorage.removeItem('microsoft_access_token');
      this.accessToken = null;
      this.refreshPage();
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

/* Style pour le formulaire d'ajout d'événement */
.add-event {
  margin-top: 20px;
  width: 80%;
  text-align: center;
}

.add-event h2 {
  font-size: 2em;
  margin-bottom: 10px;
  color: black;
}

.add-event form {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.add-event label {
  display: block;
  margin-bottom: 5px;
  color: black;
}

.add-event input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background: white;
  color: black;
  border: 1px black solid;
  border-radius: 20px;
}

.add-event button {
  background-color: #2176FF;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-event button:hover {
  background-color: #0056b3;
}
</style>

