<template>
  <div id="app">
    <Header :numCorrect="numCorrect" :numTotal="numTotal"/>
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6" offset="3">
          <QuestionBox 
          :currentQuestion="questions[index]" 
          :next="next"
          v-if="questions.length"
          :increment="increment"
          />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
//import components
import Header from './components/Header.vue'
import QuestionBox from './components/QuestionBox.vue'

export default {
  name: 'App',
  //bring components in
  components: {
    Header,
    QuestionBox
  },

  //data to be used in the component
  data() {
    return {
      questions: [], //array to store questions
      index: 0, //index of question
      numCorrect: 0, //correct answers
      numTotal: 0 //total qs answered
    }
  },

  //methods to be used in the component
  methods: {
    //next question (index)
    next() {
      this.index++
    },

    //increment count of total answered and correct answers
    //only if answer is correct
    increment(isCorrect) {
      if(isCorrect) {
        this.numCorrect++
      }

      this.numTotal++
    }
  },

  //lifecycle to retrieve questions from API
  mounted() {
    fetch('https://opentdb.com/api.php?amount=10&category=27&type=multiple', {
      method: 'get'
    })
    .then(response => {
      return response.json() //return promise result as json
    })
    .then(jsonData => {
      //assign the result to questions array
      this.questions = jsonData.results
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
