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
    <div v-else class="quiz-results-container">
      <div class="quiz-results">
        <h2>Résultats du quiz :</h2>
        <div class="result-card">
          <svg viewBox="0 0 36 36" class="circular-chart" :class="getColorClass()">
            <path class="circle-bg"
                  d="M18 2.0845
                     a 15.9155 15.9155 0 0 1 0 31.831
                     a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <path class="circle"
                  :stroke-dasharray="circleProgress"
                  d="M18 2.0845
                     a 15.9155 15.9155 0 0 1 0 31.831
                     a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <text x="18" y="20.35" class="percentage-text">{{ calculatePercentage() }}%</text>
          </svg>
        </div>
        <div class="feedback-message">
          {{ feedbackMessage }}
        </div>
        <h2 class="final-score">Note finale : {{ calculateScore() }}/{{ questions.length }}</h2>
      </div>
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
      incorrectAnswers: [],
      quizCompleted: false,
      feedbackMessage: "",
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
    async fetchFeedbackMessage() {
      try {
        console.log("fetchFeedbackMessage called");  // Point de débogage
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ` // Remplacez YOUR_OPENAI_API_KEY par votre clé API réelle
          },
          body: JSON.stringify({
            model: "gpt-4o",
            messages: [
              {role: "system", content: "You are a helpful assistant."},
              {role: "user", content: this.generatePrompt()}
            ],
            max_tokens: 1000, // Augmentez le nombre de tokens pour permettre une réponse plus longue
            temperature: 0.7
          })
        });
        const data = await response.json();
        console.log("API response:", data);  // Point de débogage
        if (data.choices && data.choices.length > 0) {
          this.feedbackMessage = this.formatFeedback(data.choices[0].message.content.trim());
        } else {
          this.feedbackMessage = "Notre Hairo doit prendre une pause, il aide un étudiant en difficulté";
        }
      } catch (error) {
        console.error("Erreur lors de l'appel à l'API OpenAI :", error);
        this.feedbackMessage = "Une erreur s'est produite lors de la génération du feedback.";
      }
    },
    generatePrompt() {
      let prompt = "Can you provide concise feedback in French, with a maximum of 1000 characters, based on the following incorrect responses? Provide a summary of the key points and concepts that need to be reviewed:\n";
      this.incorrectAnswers.forEach((answer, index) => {
        prompt += `${index + 1}. ${answer}\n`;
      });
      console.log("Generated prompt:", prompt);  // Point de débogage
      return prompt;
    },
    formatFeedback(feedback) {
      let formattedFeedback = feedback.split('\n').map(line => line.trim()).filter(line => line.length > 0).join(' ');
      if (formattedFeedback.length > 1000) {
        formattedFeedback = formattedFeedback.slice(0, 1000) + '...';
      }
      return formattedFeedback;
    },
    async finishQuiz() {
      this.quizCompleted = true;
      await this.fetchFeedbackMessage();
    },
    submitAnswer() {
      if (this.selectedAnswer === null) {
        this.selectedAnswer = 0;
      }
      const goodAnswers = this.currentQuestion.good_answers;
      const isCorrect = goodAnswers.includes(this.selectedAnswer);
      this.quizResults.push(isCorrect ? "Bonne réponse" : "Mauvaise réponse");
      if (!isCorrect) {
        if (this.currentQuestion.answers[this.selectedAnswer] === undefined) {
          this.currentQuestion.answers[this.selectedAnswer] = "Non répondue";
        }
        this.incorrectAnswers.push(this.currentQuestion.question + " : " + this.currentQuestion.answers[this.selectedAnswer]);
      }
      if (isCorrect) {
        this.score += 1;
      }
      this.currentIndex++;
      if (this.currentIndex < this.questions.length) {
        this.currentQuestion = this.questions[this.currentIndex];
        this.selectedAnswer = null;
      } else {
        this.finishQuiz();
      }
    },
    calculateScore() {
      return this.score;
    },
    calculatePercentage() {
      return Math.round((this.score / this.questions.length) * 100);
    },
    circleProgress() {
      const percentage = this.calculatePercentage();
      return `${percentage}, 100`;
    },
    getColorClass() {
      const percentage = this.calculatePercentage();
      if (percentage >= 75) {
        return 'green';
      } else if (percentage >= 50) {
        return 'orange';
      } else {
        return 'red';
      }
    },
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
  border: 5px solid #2176FF;
  border-radius: 50%;
  outline: none;
  cursor: pointer;
  margin-right: 10px;
  transition: background-color 0.3s, border-color 0.3s;
  margin-right: 20px;
}

.custom-radio input[type="radio"]:checked {
  border-color: #2176FF;
  background-color: #2176FF;
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
  position: relative;
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

.quiz-results-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 85%;
  flex-direction: column;
  margin-left: 18rem;
}

.quiz-results {
  text-align: center;
  width: 60%;
  background-color: white;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.result-card {
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
  font-size: 2rem;
}

.circular-chart {
  display: block;
  margin: 10px auto;
  max-width: 80%;
  max-height: 250px;
}

.circle-bg {
  fill: none;
  stroke: #eee;
  stroke-width: 3.8;
}

.circle {
  fill: none;
  stroke-width: 2.8;
  stroke-linecap: round;
  animation: progress 1s ease-out forwards;
}

.green .circle {
  stroke: #4caf50;
}

.orange .circle {
  stroke: #ffa500;
}

.red .circle {
  stroke: #f44336;
}

.percentage-text {
  fill: #666;
  font-family: sans-serif;
  font-size: 0.3em;
  text-anchor: middle;
}

@keyframes progress {
  0% {
    stroke-dasharray: 0 100;
  }
}

.feedback-message {
  margin-bottom: 20px;
  font-size: 1.5rem;
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
