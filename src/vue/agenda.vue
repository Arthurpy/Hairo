<template>
  <div>
    <h1>Liste des événements</h1>
    <ul>
      <li v-for="event in events" :key="event.id">{{ event.title }}</li>
    </ul>

    <!-- Bouton pour revenir au Dashboard -->
    <button @click="redirectToDashboard">Retour au Dashboard</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      events: [],
    };
  },
  mounted() {
    this.fetchEvents();
  },
  methods: {
    fetchEvents() {
      axios.get('http://localhost:8000/api/events/')
        .then(response => {
          this.events = response.data;
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des événements :', error);
        });
    },
    redirectToDashboard() {
      // Rediriger vers le Dashboard (à adapter selon ton chemin d'accès)
      this.$router.push('/dashboard');
    }
  }
};
</script>

<style scoped>
/* Ajoute du style CSS au besoin */
.agenda-container {
  background-color: #fff;
  padding: 20px; /* Ajoute un padding pour l'espace autour du contenu */
}
</style>
