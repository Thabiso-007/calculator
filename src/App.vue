<template>
  <div id="app">
    <div class="container_row mb-5">
      <Header msg="Basic Calculators"/>
    </div>
    <div class="container_row mt-5">
      <Calculator />
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Calculator from './components/Calculator.vue'

export default {
  name: 'App',
  components: {
    Header,
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
  margin-top: 0px;
  background-color: rgba(0, 0, 0, 0.7);
  width: 100%;
  height: 100vh;
}
.container_row{
  display: grid;
  width: 100%;
}
</style>
