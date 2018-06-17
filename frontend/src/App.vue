<template>
  <v-app id="app">
    <app-nav-bar/>
    <v-flex class="app__flex">
      <router-view />
    </v-flex>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',
  components: { 'app-nav-bar': NavBar }
};
</script>

<style lang="scss">
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
.app{
  &__flex{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  &__gradient{
    background-color: #FEE140;
    background-image: linear-gradient(90deg, #FA709A 0%, #FEE140 100%);
  }
  &__card{
    width: 400px;
    max-height: 80vh;
    border-radius: 2px 2px 10px 10px;
    overflow: auto;
    box-shadow: 4px 6px 20px -5px #777;
    &-header{
        min-height: 75px;
        display: flex;
        flex-direction: column;
        position: relative;
        &-title{
            color: white;
            margin:16px;
        }
        &-subtitle{
            color: white;
            text-overflow: ellipsis;
        }
    }
  }
}
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    border-radius: 10px;
    background: rgba(0,0,0,0.1);
}
::-webkit-scrollbar-thumb{
    border-radius: 10px;
    background: rgba(0,0,0,0.2);
}
::-webkit-scrollbar-thumb:hover{
  	background: rgba(0,0,0,0.4);
}
::-webkit-scrollbar-thumb:active{
  	background: rgba(0,0,0,.9);
}
</style>