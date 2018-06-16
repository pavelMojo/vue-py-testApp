<template>
  <v-app id="app">

    <v-toolbar color="white" class="nav-bar">
      <router-link to='/' >Main</router-link>

      <router-link to='/register' v-if="!user.token">Register</router-link>
      <router-link to='/login'    v-if="!user.token">Log in</router-link>
      <router-link to='/logout'   v-if="user.token">Log out</router-link>
      <router-link to='/leave'    v-if="user.token">Delete account</router-link>

      <v-menu offset-y>
        <v-btn slot="activator" class="user-form-baner" dark>Test API call</v-btn>
        <v-list>
          <v-list-tile v-for="(procedure, index) in api" :key="index" @click="testApiCall(procedure)">
            <v-list-tile-title>{{ procedure.name }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
 
    <router-view />
  </v-app>
</template>

<script>
import {pathes, calls} from './API';

export default {
  name: 'App',
  data() {
    return {
      api: calls,
      user: {},
      //setUser: this.setUser,
      students: [],
      //setStudents: this.setStudents 
    }
  },
  methods:{
    setUser(user) {
      this.user = user
    },
    setStudents(students) {
      this.students = students
    },
    testApiCall({ path, data }) {
      this.$http.post(path, data).then(
          (response) => this.show(response),
          (error) => this.show(error)
      )
    },
    // todo: show result on blank page?
    show(apiCallResult) {
      alert(JSON.stringify(apiCallResult))
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
.body{
  margin-top: 48px;
}
.nav-bar{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
a{
  color: black !important;
  text-decoration: none;
  margin: auto 20px;
}
</style>