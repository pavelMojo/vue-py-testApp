<template>
    <v-toolbar color="white" class="nav-bar">
      <a class="nav-bar-login app-gradient" v-if="user.token">Привет, {{ user.login }}</a>
      <router-link to='/' >Main</router-link>
      <router-link to='/register' >Register</router-link>
      <router-link to='/login'    >Log in</router-link>
      <router-link to='/logout'   >Log out</router-link>
      <router-link to='/leave' v-if="0"   >Delete account</router-link>

      <v-menu offset-y>
        <v-btn slot="activator" class="app-gradient" dark>Test API call</v-btn>
        <v-list>
          <template v-for="(procedure, index) in api">
            <v-subheader v-if="procedure.section" :key="procedure.section">{{ procedure.section }}</v-subheader>
            <v-list-tile v-if="procedure.name" :key="index" :disabled="procedure.type=='delete'" @click="callApi(procedure)">
              <v-list-tile-title >{{ procedure.name }}</v-list-tile-title>
            </v-list-tile>
            <v-divider v-if="procedure.divider" :key="procedure.divider"></v-divider>
          </template>
        </v-list>
      </v-menu>
    </v-toolbar>
</template>

<script>
import { testCalls as api }  from './../api/testCalls';

export default {
    data() {
        return{
            api
        };
    },
    computed:{
        user() {
            return this.$store.getters.user;
        }
    },
    methods:{
        callApi(procedure) {
            const show = (apiCallResult) => {
                // ! call $router.push with params doesnt call watch in apiResult component 
                // this.$router.push({ name: 'api', params: { apiCallResult: a }});

                const excludeBodyText = (key, value) =>
                    (typeof value === 'string' && key === 'bodyText') ? 
                        undefined : value 
        
                alert(JSON.stringify(apiCallResult, excludeBodyText, 2));
            }
  
            const { type, path, data } = procedure;
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
}
</script>

<style lang="scss">
.nav-bar{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-bottom: 30px;
  &-login{
    font-size: 200%;
    text-transform: uppercase;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-right: auto;
    cursor: default !important;
  }
}
// overwrite buildin style to show user name on the left of nav-bar
.toolbar__content{
    width: 100%;
    justify-content: flex-end;
}
</style>