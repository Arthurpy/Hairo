<template>
  <div class="bg-blue-200 h-screen text-black" style="font-family: Poppins;">
    <sidebar :activeButton="'quiz'"/>
    <div v-if="!quizCompleted" class="quiz-container flex items-center text-black">
      <div class="question-card">
        <div class="question-content">
          <h3 class="question-text">{{ currentQuestion.question }}</h3>
          <div class="question-number">
            Question {{ currentIndex + 1 }}/{{ questions.length }}
          </div>
          <ul class="answer">
            <li v-for="(answer, key) in currentQuestion.answers" :key="key" style="background-color: #D3EDFF; margin-left: 20px; margin: 10px; border-radius: 20px;">
              <label class="custom-radio">
                <input type="radio" :name="'question_' + currentIndex" :value="key" v-model="selectedAnswer"/>
                {{ answer }}
              </label>
            </li>
          </ul>
        </div>
        <button class="next-button" @click="submitAnswer">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M19.78 2.2002L24 6.4202L8.44 22.0002L0 13.5502L4.22 9.3302L8.44 13.5502L19.78 2.2002ZM19.78 5.0002L8.44 16.3602L4.22 12.1902L2.81 13.5502L8.44 19.1702L21.19 6.4202L19.78 5.0002Z" fill="white"/>
          </svg>
        </button>
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
  align-items: center;
  height: 100%;
  width: 100%;
  margin-left: 25vw;
}

.answer {
  list-style-type: none;
  padding: 0;
  font-size: 1.5rem;
}

.custom-radio {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  margin: 10px;
  margin-left: 10px;
  padding: 10px;
}

.custom-radio input[type="radio"] {
  appearance: none;
  width: 30px;
  height: 30px;
  border: 5px solid #2176FF; /* Bordure bleue transparente */
  border-radius: 50%;
  outline: none;
  cursor: pointer;
  margin-right: 10px;
  transition: background-color 0.3s, border-color 0.3s;
  margin-right: 20px;
}

.custom-radio input[type="radio"]:checked {
  border-color: #2176FF; /* Bordure bleue opaque */
  background-color: #2176FF; /* Fond bleu quand sélectionné */
}

.question-card {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 70%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative; /* Pour permettre le positionnement absolu de .question-number */
}

.question-content {
  margin-bottom: 20px;
}

.question-text {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 20px;
  width: 80%;
  color: var(--PRIMAIRE, #FFA93E);
  text-align: center;
  font-family: Poppins;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}

.question-number {
  position: absolute;
  top: -1rem;
  right: -1.5rem;
  font-size: 1rem;
  font-weight: bold;
  background: #2176FF;
  color: white;
  padding: 12px 35px;
  border-radius: 10px;
}

.next-button {
  position: absolute;
    bottom: -1rem;
    right: -1.5rem;
    background-color: #FFA93E;
    color: #ffffff;
    padding: 15px;
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

body {
  display: flex;
  width: 100vw;
  height: 100vh;
  flex-direction: row;
}

  </style>
  