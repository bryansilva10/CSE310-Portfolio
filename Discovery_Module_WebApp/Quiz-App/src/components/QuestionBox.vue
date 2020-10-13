<template>
  <div class="question-box-container">
    <b-jumbotron>
      <template v-slot:lead>
        {{currentQuestion.question}}
      </template>

      <hr class="my-4">

      <b-list-group>
        <b-list-group-item v-for="(answer,index) in shuffledAnswers" :key="index" @click.prevent="selectAnswer(index)" :class="answerClass(index)">
          {{answer}}
        </b-list-group-item>
      </b-list-group>

      <b-button variant="primary" href="#" @click="submitAnswer" :disabled="selectedIndex === null || answered">Submit</b-button>
      <b-button @click="next" variant="success" href="#">Next</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  //props of data coming from app.vue parent
  props: {
    //the prop and its type
    currentQuestion: Object,
    next: Function,
    increment: Function
  },

  //data necessary for comppnent
  data() {
    return {
      selectedIndex: null, //user selection
      correctIndex: null, //right answer
      shuffledAnswers: [], 
      answered: false //if its been already or not
    }
  },

  //to get the value of the answers, right and wrong
  computed: {
    answers() {
      let answers = [...this.currentQuestion.incorrect_answers]
      answers.push(this.currentQuestion.correct_answer)
      return answers
    }
  },

  //watch the current question for changes, to shuffle the answers
  watch: {
    currentQuestion: {
      immediate: true, //set to perform as soon as mounted
      handler() {
        this.selectedIndex = null //undo selection
        this.answered = false //undo prev answer
        this.shuffleAnswers() //shuffle
      }
    }
  },

  methods: {
    selectAnswer(index) {
      this.selectedIndex = index //assing index of selection
    },

    shuffleAnswers() {
      //grab answers, right and wrong
      let answers = [...this.currentQuestion.incorrect_answers, this.currentQuestion.correct_answer]
      //shuffle them
      this.shuffledAnswers = _.shuffle(answers)
      //assign index of the correct answer of the current question
      this.correctIndex = this.shuffledAnswers.indexOf(this.currentQuestion.correct_answer)
    },

    submitAnswer() {
      //variable to hold if correct or not
      let isCorrect = false

      //if user selection is correct
      if(this.selectedIndex === this.correctIndex) {
        isCorrect = true //change to true
      }

      //change to true
      this.answered = true

      //call increment (from parent) passing selection
      this.increment(isCorrect)

    },

    //method to deal with the right class to be assigned to user selection
    answerClass(index) {
      let answerClass = ''
      if (!this.answered && this.selectedIndex === index) {
        answerClass = 'selected'
      } else if (this.answered && this.correctIndex === index) {
        answerClass = 'correct'
      } else if (this.answered &&
        this.selectedIndex === index &&
        this.correctIndex !== index
      ) {
        answerClass = 'incorrect'
      }
      return answerClass
    }
  }
}
</script>

<style scoped>
.list-group {
  margin-bottom: 15px;
}

.list-group-item:hover {
  background: #eee;
  cursor: pointer;
}

.btn {
  margin: 0 5px;
}

.selected {
  background: lightblue;
}

.correct {
  background: lightgreen;
}

.incorrect {
  background-color: rgb(252, 99, 99);
}

</style>