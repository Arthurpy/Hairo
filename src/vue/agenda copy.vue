<template>
  <sidebar :active-button="'agenda'"/>
  <div class="bg-blue-200">
  <div class="flex flex-col ml-80">
    <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
      <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Agenda</h1>
    </div>
  </div>
    <div class="main-content h-screen" style="display: flex; flex-direction: column; justify-content: center; align-items: center; max-width: 800px; margin: auto;">
      <vue-cal :events="events" style="height: 500px; width: 1200px; margin: 80px; margin-right: -100px;" class="vuecal--blue-theme vuecal__event--microsoft-event"></vue-cal>
      <div style="display: flex; justify-content: space-between; width: 160%; margin-bottom: 300px; margin-right: -250px;">
      <button v-if="!accessToken" @click="openMicrosoftLogin" class="my-button btn-hover" style="width: 250px; height: 80px;">Se connecter avec Microsoft</button>
      <button class="my-button btn-hover" @click="redirectToDashboard" style="width: 250px; height: 80px;">Retour au Dashboard</button>
      <button class="my-button btn-hover" @click="showEventForm = true" style="width: 250px; height: 80px;">Nouvel évènement</button>
      <button class="my-button btn-hover" @click="showDeleteModal = true" style="width: 250px; height: 80px;">Retirer un évènement</button>
      <button class="my-button btn-hover" @click="" style="width: 250px; height: 80px;">Conseils de planning</button>
    </div>
      <div v-if="showEventForm" class="event-modal">
      <input v-model="newEvent.title" placeholder="Event Title" style="background-color: aliceblue;">
      <input v-model="newEvent.start" type="datetime-local" placeholder="Start Time" style="background-color: aliceblue;">
      <input v-model="newEvent.end" type="datetime-local" placeholder="End Time" style="background-color: aliceblue;">
      <textarea v-model="newEvent.description" placeholder="Description" style="background-color: aliceblue;"></textarea>
      <div style="display: flex; justify-content: space-between; width: 23%; margin-right: -250px;">
      <button class="my-button" @click="addEventToCalendar">Valider</button>
      <button class="my-button" @click="showEventForm = false">Annuler</button>
    </div>
    </div>
      <div v-if="showDeleteModal" class="delete-modal">
        <h3>Select an Event to Delete</h3>
        <ul>
          <li v-for="event in events" :key="event.id">
            {{ event.title }} - {{ event.start }}
            <button @click="prepareEventForDeletion(event)">Delete</button>
          </li>
        </ul>
        <button @click="showDeleteModal = false">Close</button>
      </div>
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
      showDeleteModal: false,
      eventToDelete: null,
      showEventForm: false,
      newEvent: {
        id: '',
        title: '',
        start: '',
        end: '',
        description: ''
      },
      events: [],
      isLightMode: true,
      accessToken: null,
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
    async addEventToCalendar() {
    try {
      const event = {
        subject: this.newEvent.title,
        start: {
          dateTime: this.newEvent.start,
          timeZone: "UTC"
        },
        end: {
          dateTime: this.newEvent.end,
          timeZone: "UTC"
        },
        body: {
          contentType: "text",
          content: this.newEvent.description
        }
      };
      const response = await fetch('https://graph.microsoft.com/v1.0/me/events', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + this.accessToken,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(event)
      });
      if (!response.ok) {
        throw new Error(`API request failed: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      this.events.push({
        id: data.id,
        title: this.newEvent.title,
        start: this.newEvent.start,
        end: this.newEvent.end,
        description: this.newEvent.description
      });

      this.newEvent = {
        id: '',
        title: '',
        start: '',
        end: '',
        description: ''
      };
      this.showEventForm = false;
      this.fetchCalendarData();
    } catch (error) {
      console.error('Error adding event to calendar:', error);
    }
  },
  prepareEventForDeletion(event) {
    this.eventToDelete = event;
    if (confirm(`Are you sure you want to delete the event: ${event.title}?`)) {
      this.deleteEvent();
    }
  },
  async deleteEvent() {
  if (!this.eventToDelete) return;

  try {
    const response = await fetch(`https://graph.microsoft.com/v1.0/me/events/${this.eventToDelete.id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      alert('Event deleted successfully');
      this.events = this.events.filter(event => event.id !== this.eventToDelete.id);
      this.eventToDelete = null;
      this.showDeleteModal = false;
    } else {
      throw new Error(`Failed to delete the event: ${response.status} ${response.statusText}`);
    }
    this.fetchCalendarData();
  } catch (error) {
    alert(`Error deleting the event: ${error.message}`);
  }
  },
  refreshPage() {
    window.location.reload();
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
  background-color: #2176FF;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 10px;
  transition: background-color 0.3s ease;
}

.vuecal__event--microsoft-event {
  background-color: #fdc2217d;
}

.btn-hover:hover {
    background-color: #FFA93E;
    border-radius: 20px;
}

.event-modal {
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -20%);
  background: rgb(247, 113, 113);
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  z-index: 100;
}

.delete-modal {
  position: fixed;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -30%);
  background: white;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  z-index: 100;
}
</style>
