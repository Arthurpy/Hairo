<template>
    <div class="bg-blue-200 h-screen text-black">
      <sidebar :activeButton="'quiz'"/>
      <div v-if="!quizCompleted" class="quiz-container flex justify-center items-center text-black">
        <div class="question-card">
          <div class="question-content">
            <h3 class="question-text">{{ currentQuestion.question }}</h3>
            <ul>
              <li v-for="(answer, key) in currentQuestion.answers" :key="key">
                <label>
                  <input type="radio" :name="'question_' + currentIndex" :value="key" v-model="selectedAnswer"/>
                  {{ answer }}
                </label>
              </li>
            </ul>
          </div>
          <button class="next-button" @click="submitAnswer">Suivant</button>
        </div>
      </div>
      <div v-else class="quiz-results">
        <h2>Résultats du quiz :</h2>
        <ul>
          <li v-for="(result, index) in quizResults" :key="index">
            Question {{ index + 1 }} : {{ result }}
          </li>
        </ul>
        <h2 class="final-score">Note finale : {{ calculateScore() }}/20</h2>
      </div>
    </div>
  </template>
  
  <script>
  import sidebar from './../components/sidebar.vue';
  
  export default {
    name: 'quiz',
    components: {
      sidebar,
    },
    data() {
      return {
        questions: [],
        currentIndex: 0,
        currentQuestion: null,
        selectedAnswer: null,
        quizResults: [],
        quizCompleted: false,
        score: 0
      };
    },
    created() {
      this.fetchQuestions();
    },
    methods: {
      async fetchQuestions() {
        try {
          const response = await fetch("http://localhost:8000/media/qcms/Myologie.json");
          const data = await response.json();
          this.questions = data.questions;
          this.currentQuestion = this.questions[this.currentIndex];
        } catch (error) {
          console.error("Erreur lors de la récupération des questions :", error);
        }
      },
      submitAnswer() {
        // Vérifier si une réponse a été sélectionnée
        if (this.selectedAnswer === null) {
          alert("Veuillez sélectionner une réponse !");
          return;
        }
        // Stocker le résultat de la question actuelle
        const goodAnswers = this.currentQuestion.good_answers;
        const isCorrect = goodAnswers.includes(this.selectedAnswer);
        this.quizResults.push(isCorrect ? "Bonne réponse" : "Mauvaise réponse");
        // Ajouter la note
        if (isCorrect) {
          this.score += 1;
        }
        // Passer à la question suivante
        this.currentIndex++;
        if (this.currentIndex < this.questions.length) {
          this.currentQuestion = this.questions[this.currentIndex];
          this.selectedAnswer = null; // Réinitialiser la réponse sélectionnée
        } else {
          // Si toutes les questions ont été répondues, marquer le quiz comme terminé
          this.quizCompleted = true;
        }
      },
      calculateScore() {
        // Calculer la note finale
        return this.score;
      }
    }
  };
  </script>
  
  <style scoped>
  .quiz-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
  
  .question-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 400px;
  }
  
  .question-content {
    margin-bottom: 20px;
  }
  
  .question-text {
    text-align: center;
  }
  
  .next-button {
    position: absolute;
    bottom: 20px;
    right: 20px;
    background-color: orange;
    color: #ffffff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .next-button:hover {
    background-color: #ff8c00;
  }
  
  .quiz-results {
    text-align: center;
  }
  
  .final-score {
    margin-top: 20px;
  }
  </style>
  