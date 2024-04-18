<template>
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto'; // Importer Chart.js
  
  export default {
    props: {
      chartData: {
        type: Object,
        required: true,
      },
    },
    mounted() {
      this.renderChart(); // Appeler la méthode pour afficher le graphique lors du montage du composant
    },
    methods: {
      renderChart() {
        const chartCanvas = this.$refs.chartCanvas; // Récupérer la référence du canvas
  
        // Créer le graphique camembert
        new Chart(chartCanvas, {
          type: 'pie', // Type de graphique camembert
          data: {
            labels: this.chartData.labels, // Les étiquettes du graphique (noms des sections)
            datasets: [
              {
                data: this.chartData.data, // Les données du graphique (valeurs des sections)
                backgroundColor: this.chartData.backgroundColor || [], // Couleurs de fond des sections (optionnel)
                borderColor: this.chartData.borderColor || [], // Couleurs de bordure des sections (optionnel)
                borderWidth: this.chartData.borderWidth || 1, // Largeur de la bordure des sections (optionnel)
              },
            ],
          },
          options: this.chartData.options || {}, // Options du graphique (optionnel)
        });
      },
    },
  };
  </script>
  