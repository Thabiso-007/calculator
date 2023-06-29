<template>
  <div id="app">
    <div class="container_row mt-5">
      <Calculator />
    </div>
  </div>
</template>

<script>
import Calculator from './components/Calculator.vue'

export default {
  name: 'App',
  components: {
    Calculator
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  margin: 0px;
  padding-top: 200px;
  background-color: rgba(0, 0, 0, 0.7);
  width: 100%;
  height: 97.5vh;
}
.container_row{
  display: grid;
  width: 100%;
}
</style>
