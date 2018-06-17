<template>
  <v-app id="app">
    <v-toolbar color="white" class="nav-bar">
      
      <router-link to='/' >Main</router-link>
      <router-link to='/register' v-if="!user.token">Register</router-link>
      <router-link to='/login'    v-if="!user.token">Log in</router-link>
      <router-link to='/logout'   v-if="user.token">Log out</router-link>
      <router-link to='/leave'    v-if="user.token">Delete account</router-link>

      <v-menu offset-y>
        <v-btn slot="activator" class="nav-bar-api-btn" dark>Test API call</v-btn>
        <v-list>
          <template v-for="(procedure, index) in api">
            <v-subheader v-if="procedure.section" :key="procedure.section">{{ procedure.section }}</v-subheader>
            <v-list-tile v-if="procedure.name" :key="index" :disabled="procedure.type=='delete'" @click="testApiCall(procedure)">
              <v-list-tile-title >{{ procedure.name }}</v-list-tile-title>
            </v-list-tile>
            <v-divider v-if="procedure.divider" :key="procedure.divider"></v-divider>
          </template>
        </v-list>
      </v-menu>
    </v-toolbar>
 
    <router-view />
  </v-app>
</template>

<script>
import {pathes, testCalls} from './API';

export default {
  name: 'App',
  data() {
    return {
      api: testCalls,
      user: {},
      students: [],
    }
  },
  methods:{
    setUser(user) {
      this.user = user
    },
    setStudents(students) {
      this.students = students
    },
    testApiCall({ type, path, data }) {
      const show = (apiCallResult) => 
        this.$router.push({ 
          name: 'api',
          params: { apiCallResult }
        });

      switch(type){
        case 'post':
          this.$http.post(path, data).then(
            (response) => show(response),
            (error) => show(error)
          );
          break;
        case 'get':
          let params = '';
          for (const key of Object.keys(data))
            params = params + `${key}="${data[key]}"&`
          
          this.$http.get(`${path}/${params}`).then(
            (response) => show(response),
            (error) => show(error)
          );
          break;
        default:
          throw `Not implement for type '${type}'`;
      }
    },
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
.body{
  margin-top: 48px;
}
.nav-bar{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-bottom: 30px;
}
.nav-bar-api-btn{
    background-color: #FEE140;
    background-image: linear-gradient(90deg, #FA709A 0%, #FEE140 100%);
}
</style>