<template>
  <div>
    <sidebar :active-button="'agenda'"/>
    <div class="bg-blue-200">
      <div class="flex flex-col ml-80">
        <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-10 py-16">
          <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Agenda</h1>
        </div>
      </div>
      <div class="main-content h-screen" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div class="carousel-container">
          <button @click="prevMonth" class="carousel-button">‹</button>
          <div class="calendars-wrapper">
            <vue-cal
              v-for="index in 3"
              :key="index"
              :default-view="'month'"
              :time="getMonthTime(index)"
              :events="events"
              style="height: 500px; width: 400px; margin: 0 10px; background-color: white; border-radius: 10px; padding: 20px;"
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
                {{ event.title }} - {{ new Date(event.start).toLocaleDateString() }}
              </li>
            </ul>
          </div>
        </div>
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
      events: [],
      currentMonth: new Date(),
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
  },
  components: {
    sidebar,
    VueCal,
  },
  computed: {
    sortedEvents() {
      return this.events.sort((a, b) => new Date(a.start) - new Date(b.start));
    }
  },
  methods: {
    openMicrosoftLogin() {
      window.location.href = 'http://localhost:8000/agenda-login/';
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
}
</style>
