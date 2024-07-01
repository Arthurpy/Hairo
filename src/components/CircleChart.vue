<template>
  <div>
    <canvas ref="circleChart"></canvas>
  </div>
</template>

<script>
import { Chart } from 'chart.js';

export default {
  name: 'CircleChart',
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
      new Chart(this.$refs.circleChart, {
        type: 'doughnut',
        data: this.chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },
  },
};
</script>

<style scoped>
canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>
