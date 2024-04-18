<template>
    <div>
      <canvas ref="lineChartCanvas"></canvas>
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
      chartOptions: {
        type: Object,
        default: () => ({
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        }),
      },
    },
    mounted() {
      this.renderLineChart();
    },
    methods: {
      renderLineChart() {
        const ctx = this.$refs.lineChartCanvas.getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: this.chartData,
          options: this.chartOptions,
        });
      },
    },
  };
  </script>
  