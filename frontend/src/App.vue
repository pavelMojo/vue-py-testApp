<template>
  <v-app id="app">

    <div>
       <router-link to='/login'>Login</router-link>
      <router-link to='/register'>Register</router-link>
      <router-link to='/'>Main</router-link>
    </div>
 
    <router-view/>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      API: {
        register: `localhost:8080/register`,
        login:    `localhost:8080/login`,
        logout:   `localhost:8080/logout`,
        leave:    `localhost:8080/leave`,
        students: `localhost:8080/students`,
        student:  `localhost:8080/student`,
      },
      user: {},
      students: [], 
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
