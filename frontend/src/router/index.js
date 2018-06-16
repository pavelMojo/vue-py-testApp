import Vue from 'vue'
import Router from 'vue-router'
import vueResource from 'vue-resource'

import Main from '@/components/main';
import loginForm from '@/components/loginForm';
import RegisterForm from '@/components/registerForm';

Vue.use(Router)
Vue.use(vueResource)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main page',
      component: Main
    },
    {
      path: '/login',
      name: 'Log in',
      component: loginForm
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterForm
    }
  ],
  mode: 'history'
})
