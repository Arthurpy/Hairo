<template>
  <div>
    <sidebar :active-button="'dashboard'"/>
    <div class="bg-blue-200" style="margin-left: 18rem; display: flex; flex-direction: column; align-items: center; min-height: 100vh;">
      <div class="flex flex-col">
        <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] rounded-lg justify-between items-center mt-10 py-16">
          <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10" style="color: #2176FF; font-size: 3rem;">Dashboard</h1>
          <img src="../assets/Bonhommecp.png" alt="profile" class="rounded-full mr-10" style="height: auto;"/>
        </div>
      </div>
      <div class="main-content p-8" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div class="flex flex-row w-[70vw]" style="color: aliceblue;">
          <div class="flex flex-row w-1/2 h-[300px] rounded-lg">
            <vue-cal v-for="index in 1"
              :key="index"
              :default-view="'month'"
              :events="events"
              :locales="locales"
              :locale="'fr'"
              :editable="true"
              @event-change="onEventChange"
              style="margin: 0; height: 100%; background-color: white; border-radius: 10px; padding: 20px; color: black; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"
              class="w-full" :attributes="calendarEvents" />
          </div>
          <div class="flex flex-col bg-white w-1/2 h-[300px] rounded-lg ml-4 p-4">
            <div class="h-[70%] flex flex-row m-3 text-[#2176FF]">
              <img :src="profilePicture" alt="profile" class="w-[70px] h-[70px]"/>
              <div class="flex flex-col ml-4 mt-2">
                <h4 class="font-bold text-[#2176FF]">{{ profile.name }}</h4>
                <h4>{{ profile.prenom }}</h4>
              </div>
              <div class="flex flex-col ml-4 mt-2">
                <h4 class="font-bold text-[#FFA93E]">Moyenne :</h4>
                <h4>{{ profile.moyenne_visee }}</h4>
              </div>
            </div>
            <div class="flex flex-row justify-between text-[#2176FF]">
              <div class="mx-5">
                <h4>tutorat : {{ profile.tutorat }}</h4>
                <h4>faculté : {{ profile.faculte }}</h4>
              </div>
              <div class="mx-5">
                <h4>{{ profile.rank }}</h4>
              </div>
            </div>
            <div class="flex flex-row justify-around mb-4 mt-6">
              <div class="flex btn bg-[#2176FF] font-semibold">voir le profil</div>
              <div class="flex btn bg-[#2176FF] font-semibold" disabled>messagerie</div>
            </div>
          </div>
        </div>
        <div class="relative mt-4 bg-white text-black rounded-lg overflow-hidden justify-around items-center flex flex-row p-6 w-[70vw] at_work">
            <div class="flex flex-col items-center my-4 blur-[4px]" ref="chartContainer">
                <h4 class="text-[#2176FF] font-semibold">Moyenne des QCMs</h4>
                <ChartCamembert :chartData="pieChartData"/>
            </div>
            <div class="flex flex-col items-center font-semibold blur-[4px]">
                <h4 class="text-[#2176FF]">Temps de Travail</h4>
                <LineChart :chartData="lineChartData"/>
            </div>
            <div class="flex flex-col items-center font-semibold blur-[4px]">
                <h4 class="text-[#2176FF]">Notes des QCMs récents</h4>
                <div class="flex flex-row justify-around w-full">
                    <div class="w-32 h-32 relative flex items-center justify-center">
                        <CircleChart :chartData="circleChartData1"/>
                    </div>
                    <div class="w-32 h-32 relative flex items-center justify-center">
                        <CircleChart :chartData="circleChartData2"/>
                    </div>
                    <div class="w-32 h-32 relative flex items-center justify-center">
                        <CircleChart :chartData="circleChartData3"/>
                    </div>
                </div>
            </div>
            <div class="absolute inset-0 flex justify-center items-center">
                <p class="text-[#2176FF] text-[2rem] font-semibold bg-white bg-opacity-40 rounded p-2">Continue de travailler pour avoir ses informations</p>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sidebar from '../components/sidebar.vue';
import ChartCamembert from '../components/ChartCamembert.vue';
import LineChart from '../components/LineChart.vue';
import CircleChart from '../components/CircleChart.vue';
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
  name: 'dashboard',
  components: {
    sidebar,
    ChartCamembert,
    LineChart,
    CircleChart,
    VueCal,
  },
  data() {
    return {
      profile: {
        name: '',
        prenom: '',
        faculte: '',
        tutorat: '',
        moyenne_visee: '',
        rank: '',
      },
      profilePicture: '',
      pieChartData: {
        labels: ['a faire', 'rater', 'fini'],
        title: 'resultat des QCMs',
        data: [60, 10, 30],
        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
        borderWidth: 1,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          width: 30,
          height: 30,
          plugins: {
            legend: {
              display: true,
              position: 'bottom',
            },
          },
        },
      },
      lineChartData: {
        labels: ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil'],
        datasets: [
          {
            label: 'heures de travail / mois',
            data: [],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false,
          },
        ],
      },
      circleChartData1: {
        labels: ['QCM 1'],
        datasets: [
          {
            label: 'Notes en %',
            data: [85, 15],
            backgroundColor: ['#4CAF50', '#FFCE56'],
            borderWidth: 1,
          },
        ],
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      },
      circleChartData2: {
        labels: ['QCM 2'],
        datasets: [
          {
            label: 'Notes en %',
            data: [60, 40],
            backgroundColor: ['#36A2EB', '#FFCE56'],
            borderWidth: 1,
          },
        ],
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      },
      circleChartData3: {
        labels: ['QCM 3'],
        datasets: [
          {
            label: 'Notes en %',
            data: [70, 30],
            backgroundColor: ['#FF6384', '#FFCE56'],
            borderWidth: 1,
          },
        ],
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      },
      calendarEvents: [],
    };
  },
  mounted() {
    this.$refs.chartContainer.style.transform = 'scale(0.67)';
    this.fetchProfileData();
    this.fetchWorkHoursData();
  },
  methods: {
    async fetchProfileData() {
      const token = localStorage.getItem('authToken');
      if (!token) {
        console.error('No token found in localStorage');
        return;
      }

      try {
        const response = await fetch('http://localhost:8000/api/loadSettings', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.profile = data.profile;
        this.profilePicture = data.picture || '../src/assets/logo.png';
        console.log('Profile data fetched:', data);
      } catch (error) {
        console.error('Error fetching profile data:', error.message);
      }
    },
    async fetchWorkHoursData() {
      const token = localStorage.getItem('authToken');
      if (!token) {
        console.error('No token found in localStorage');
        return;
      }

      try {
        const response = await fetch('/api/work-hours', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.lineChartData.datasets[0].data = data;
      } catch (error) {
        console.error('Error fetching work hours data:', error.message);
      }
    },
  },
};
</script>

<style scoped>
h1 {
  color: black;
  font-size: 1.5rem;
}

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

.vuecal {
  background-color: white;
  border-radius: 7px;
  color : #2176FF;;
}

.vuecal__weekdays-headings {
    border-bottom: 1px solid #ddd;
    margin-bottom: -1px;
    font-size: x-small;
}

.vuecal__no-event {
    padding-top: 1em;
    color: #aaa;
    justify-self: flex-start;
    margin-bottom: auto;
    font-size: x-small;
}

</style>
