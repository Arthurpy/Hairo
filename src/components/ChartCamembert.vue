<template>
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto'; 
  
  export default {
    props: {
      chartData: {
        type: Object,
        required: true,
      },
    },
    mounted() {
      this.renderChart();
    },
    methods: {
      renderChart() {
        const chartCanvas = this.$refs.chartCanvas;
  
        // Créer le graphique camembert
        new Chart(chartCanvas, {
          type: 'pie',
          data: {
            labels: this.chartData.labels,
            datasets: [
              {
                data: this.chartData.data,
                backgroundColor: this.chartData.backgroundColor || [],
                borderColor: this.chartData.borderColor || [],
                borderWidth: this.chartData.borderWidth || 1,
              },
            ],
          },
          options: this.chartData.options || {},
        });
      },
    },
  };
  </script>
  