<template>
  <div>
    <b-nav tabs>
      <b-nav-item disabled><b>Fancy Quiz App</b></b-nav-item>
      <b-nav-item disabled>Counter: {{ numCorrect }}/{{ numTotal }}</b-nav-item>
    </b-nav>
  </div>
</template>

<script>
export default {
  //props of data coming from parent(app.vue)
  props: [
    'numCorrect',
    'numTotal'
  ]
}
</script>

<style>

</style>