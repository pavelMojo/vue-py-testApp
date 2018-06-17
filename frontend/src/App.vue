<template>
  <v-app id="app">
    <app-nav-bar/>
    <router-view />
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',
  components: {
    'app-nav-bar': NavBar
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
a{
  color: black !important;
  text-decoration: none;
  margin: auto 20px;
}
.gradient-background{
    background-color: #FEE140;
    background-image: linear-gradient(90deg, #FA709A 0%, #FEE140 100%);
}
</style>