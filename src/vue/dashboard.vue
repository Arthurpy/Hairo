<template>
    <div class="bg-blue-200 flex">
      <sidebar :activeButton="'dashboard'"/>
      <div class="flex flex-col ml-80 h-screen">
        <div class="flex bg-white text-[#2176FF] w-[70vw] h-[56px] ml-[50px] rounded-lg justify-between items-center mt-6 py-16">
          <h1 class="search-title text-[#2176FF] text-5xl font-bold flex items-center ml-10">Dashboard</h1>
          <img src="../assets/Rocket.png" alt="search" class="w-auto h-[150px] drop-shadow-lg" />
        </div>
        <div class="flex flex-row">
          <div class="flex flex-row bg-black w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg">
            <div class="w-[50%]">
              <h4> Dates proches</h4>
            </div>
            <div class="bg-[#2176FF] w-[50%] rounded-r-lg">
              ffw
            </div>
          </div>
          <div class="flex flex-col bg-white w-1/2 ml-[50px] mt-[30px] rounded-lg">
            <div class="h-[70%] flex flex-row m-3 text-[#2176FF]">
              <img src="../assets/PP.png" alt="profile" class="w-[70px] h-[70px]"/>
              <div class="flex flex-col ml-4 mt-2">
                <h4 class="font-bold text-[#FFA93E]">Arthur Py</h4>
                <h4 class="">P1 2024</h4>
              </div>
              <div class="flex flex-col ml-4 mt-2">
                <h4 class="font-bold text-[#FFA93E]">Moyenne</h4>
                <h4 class="">12.5</h4>
              </div>
            </div>
            <div class="flex flex-row justify-between text-[#2176FF] ">
              <div class="mx-5 ">
                <h4>Tutorat Médecine </h4>
                <h4>FAC de Bordeaux Montesquieu</h4>
              </div>
              <div class=" mx-5">
                <h4>Groupe 3</h4>
                <h4>89/460</h4>
              </div>
            </div>
            <div class="flex flex-row justify-around mb-4 mt-6">
              <div class="flex btn bg-[#2176FF] font-semibold">voir le profil</div>
              <div class="flex btn bg-[#2176FF] font-semibold " disabled>messagerie</div>
            </div>
          </div>
        </div>
        <div class="mt-[40px] bg-white text-black ml-[50px] rounded-lg overflow-hidden justify-around items-center flex flex-row p-6">
            <div class="flex flex-col items-center my-4 ">
                <h4 class="text-[#2176FF] font-semibold">Moyenne des QCMs</h4>
                <ChartCamembert :chartData="pieChartData" />
            </div>
            <div class="flex flex-col items-center font-semibold">
                <h4 class="text-[#2176FF]"> Temps de Travail </h4>
                <LineChart :chartData="lineChartData" />
            </div>
        </div>
        <div class="flex flex-row">
          <div class="flex flex-col bg-white justify-around w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg text-[#2176FF]">
              <h4 class=" text-xl font-bold ml-4 mt-4 "> Dernière révision </h4>
              <div class="bg-blue-200 flex flex-row justify-between font-semibold m-4 rounded-xl items-center ">
                <h4 class="ml-3 ">theme 1</h4>
                <h4> 2h </h4>
                <h4> 81% </h4>
                <div class="btn bg-[#FDC221] text-white">Reprendre</div>
              </div>
              <div class="bg-blue-200 flex flex-row justify-between font-semibold m-4 rounded-xl items-center ">
                <h4 class="ml-3 ">theme 2</h4>
                <h4> 2h </h4>
                <h4> 81% </h4>
                <div class="btn bg-[#FDC221] text-white">Reprendre</div>
              </div>
              <div class="bg-blue-200 flex flex-row justify-between font-semibold m-4 rounded-xl items-center">
                <h4 class="ml-3 ">theme 3</h4>
                <h4> 2h </h4>
                <h4> 81% </h4>
                <div class="btn bg-[#FDC221] text-white">Reprendre</div>
              </div>
          </div>
          <div class="flex flex-row bg-white justify-around w-[50%] h-[219px] ml-[50px] mt-[30px] rounded-lg text-[#2176FF]">
                <div class="bg-blue-200 flex flex-col justify-between font-semibold m-4 rounded-xl items-center ">
                    <h4 class="mt-3 ">theme 1</h4>
                    <h4> 2h </h4>
                    <h4> 81% </h4>
                    <div class="btn bg-[#FDC221] text-white">Reprendre</div>
                </div>
                <div class="bg-blue-200 flex flex-col justify-between font-semibold m-4 rounded-xl items-center ">
                    <h4 class="mt-3 ">theme 2</h4>
                    <h4> 2h </h4>
                    <h4> 81% </h4>
                    <div class="btn bg-[#FDC221] text-white">Reprendre</div>
                </div>
                <div class="bg-blue-200 flex flex-col justify-between font-semibold m-4 rounded-xl items-center ">
                    <h4 class="mt-3 ">theme 3</h4>
                    <h4> 2h </h4>
                    <h4> 81% </h4>
                    <div class="btn bg-[#FDC221] text-white">Reprendre</div>
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
  
  export default {
    name: 'dashboard',
    components: {
      sidebar,
      ChartCamembert,
      LineChart,
    },
    created() {
      this.checkUserLoggedIn();
      console.log(localStorage.getItem('authToken'));
    },
    data() {
      return {
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
              data: [120, 150, 170, 200, 180, 160, 190],
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 2,
              fill: false,
            },
          ],
        },
      };
    },
    methods: {
      checkUserLoggedIn() {
        if (!localStorage.getItem('authToken')) {
          this.$router.push('/login');
        }
      }
    }
  };
  </script>
  
  <style>
  h1 {
    color: black;
    font-size: 1.5rem;
  }
  </style>
  