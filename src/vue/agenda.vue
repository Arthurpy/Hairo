<template>
  <div>
    <sidebar :active-button="'agenda'"/>
    <div class="bg-blue-200" style="margin-left: 18rem; display: flex; flex-direction: column; align-items: center;">
      <div class="main-content p-8" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div class="flex flex-col w-[80%]">
          <div class="flex bg-white text-[#2176FF] h-[56px] rounded-lg justify-between items-center mt-10 py-16 mb-8">
            <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Agenda</h1>
            <button @click="logout" class="bg-red-500 text-white py-2 px-4 rounded-lg mr-10">Déconnexion</button>
          </div>
        </div>
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
              style="height: 500px; width: 400px; background-color: white; border-radius: 10px; padding: 20px; color: black; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"
              class="custom-vuecal"
            ></vue-cal>
          </div>
        </div>
        <div class="event-list">
          <h2>Événements à venir</h2>
          <div class="events-container">
            <ul v-if="sortedEvents.length > 0">
              <li v-for="event in sortedEvents" :key="event.id">
                {{ event.title }} - {{ new Date(event.start).toLocaleDateString('fr-FR') }}
              </li>
            </ul>
            <p v-else>Aucun événement à venir</p>
          </div>
        </div>
        <div class="revision-planner">
          <h2>Planificateur de Révision</h2>
          <form @submit.prevent="generateRevisionPlan">
            <label for="weekly-hours">Heures de révision hebdomadaires:</label>
            <input type="number" id="weekly-hours" v-model="weeklyHours" required>
            <label for="session-length">Durée de chaque session (en heures):</label>
            <input type="number" id="session-length" v-model="sessionLength" required>
            <button type="submit">Générer le planning</button>
          </form>
        </div>
        <div class="add-event">
          <h2>Ajouter un événement</h2>
          <form @submit.prevent="createEvent">
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
    <!-- Modal -->
    <div v-if="showModal" class="modal-agenda">
      <div class="modal-content-agenda">
        <span class="close" @click="closeModal">&times;</span>
        <p v-if="loadingMessage">{{ loadingMessage }}</p>
        <p v-else>{{ modalMessage }}</p>
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
        color: '#2176FF'
      },
      locales: {
        'fr': fr
      },
      showModal: false,
      modalMessage: '',
      loadingMessage: ''
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
      window.location.href = 'http://localhost:8000/agenda-login/';
    },
    fetchCalendarData() {
      console.log('Fetching calendar data');
      const headers = new Headers({
        'Authorization': `Bearer ${localStorage.getItem('microsoft_access_token')}`,
        'Content-Type': 'application/json'
      });
      const url = 'https://graph.microsoft.com/v1.0/me/calendars';
      fetch(url, { headers })
        .then(response => response.json())
        .then(data => {
          console.log('Calendars data:', data);
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
          console.log('Calendars events data:', calendarsData);
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
                  color: event.color ? event.color : '#2176FF'
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
        console.log('Generating revision plan');
        console.log('Weekly hours:', this.weeklyHours);
        console.log('Session length:', this.sessionLength);
        
        this.loadingMessage = 'En attente de la réponse...';
        this.showModal = true;
        
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer sk-proj-1LF3pVb76eEUghxqa3ePT3BlbkFJ4kjaCJoEg393npfDYse3`
          },
          body: JSON.stringify({
            model: 'gpt-4',
            messages: [
              { role: 'system', content: 'You are a helpful assistant.' },
              { role: 'user', content: `Plan a study schedule with the following criteria: Weekly study hours: ${this.weeklyHours}, Session length in hours: ${this.sessionLength}, using the J method. Answer in French. The J method consists of reviewing concepts at regular intervals, more and more spaced, to reinforce long-term memorization.` }
            ],
            max_tokens: 1500,
            temperature: 0.7
          })
        });
        const data = await response.json();

        if (data.choices && data.choices.length > 0) {
          const scheduleText = data.choices[0].message.content.trim();

          this.modalMessage = scheduleText;
          this.loadingMessage = '';
          console.log('Schedule:', scheduleText);

          const schedule = this.parseSchedule(scheduleText);

          for (let event of schedule) {
            await this.addEvent(event.title, event.start, event.end);
          }
        } else {
          console.error('No choices found in OpenAI response');
          this.modalMessage = 'Aucune réponse valide reçue.';
          this.loadingMessage = '';
        }
      } catch (error) {
        console.error('Error:', error);
        this.modalMessage = 'Erreur lors de la génération du plan de révision.';
        this.loadingMessage = '';
      }
    },
    parseSchedule(scheduleText) {
      const lines = scheduleText.split('\n');
      const schedule = [];

      for (let line of lines) {
        const parts = line.split(' - ');
        if (parts.length === 3) {
          schedule.push({
            title: parts[0],
            start: parts[1],
            end: parts[2]
          });
        }
      }

      return schedule;
    },
    async addEvent(title, start, end, color = '#2176FF') {
      console.log('Adding event:', title, start, end, color);
      const newEvent = {
        subject: title,
        start: {
          dateTime: new Date(start).toISOString(),
          timeZone: 'UTC'
        },
        end: {
          dateTime: new Date(end).toISOString(),
          timeZone: 'UTC'
        },
        body: {
          contentType: 'HTML',
          content: ''
        },
        color: color
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
        console.log('Event added:', data);

        this.events.push({
          id: data.id,
          start: new Date(start),
          end: new Date(end),
          title: title,
          color: color,
          class: 'custom-event',
          background: true,
        });

        this.newEvent = {
          title: '',
          start: '',
          end: '',
          color: '#2176FF'
        };
      } catch (error) {
        console.error('Error adding event:', error);
      }
    },
    async createEvent() {
      await this.addEvent(this.newEvent.title, this.newEvent.start, this.newEvent.end, this.newEvent.color);
    },
    onEventChange({ event, newStart, newEnd }) {
      const updatedEvent = this.events.find(e => e.id === event.id);
      if (updatedEvent) {
        updatedEvent.start = newStart;
        updatedEvent.end = newEnd;
        this.updateEventOnServer(updatedEvent);
      }
    },
    updateEventOnServer(event) {
      console.log('Updating event on server:', event);
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
          color: event.color
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
    closeModal() {
      this.showModal = false;
      this.modalMessage = '';
      this.loadingMessage = '';
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
  width: 80%;
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
  color: #000000;
  min-height: 150px;
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

.modal-agenda {
  color: black;
    margin-left: 18rem;
    display: flex;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 82%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  border-radius: 10px;
}

.modal-content-agenda {
  background-color: white;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  border-radius: 10px;
  height: fit-content;
  padding: 50px;
    line-height: 2;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
