import Vue from 'vue';
import Router from 'vue-router'

import StudentsList from '@/components/StudentsList';
import UserForm from '@/components/UserForm';
import ApiResult from '@/components/ApiResult';
import NotFoundComponent from '@/components/NotFound';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: StudentsList,
    },
    {
      path: '/api',
      name: 'api',
      component: ApiResult,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: UserForm,
      props: {
        type: 'Log in',
      }
    },
    {
      path: '/register',
      name: 'register',
      component: UserForm,
      props: {
        type: 'Register',
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: UserForm,
      props: {
        type: 'Log out',
      }
    },
    { path: '*', component: NotFoundComponent }
  ],
  mode: 'history'
});