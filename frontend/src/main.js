import Vue from 'vue';
import Vuetify from 'vuetify';
import Router from 'vue-router';
import vueResource from 'vue-resource';
import 'vuetify/dist/vuetify.min.css';

import router from './router';
import store from './store'
import App from './App';

Vue.use(Vuetify);
Vue.use(vueResource);

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})