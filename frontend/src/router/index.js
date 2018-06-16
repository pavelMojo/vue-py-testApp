import Router from 'vue-router'

import StudentsList from '@/components/studentsList';
import UserForm from '@/components/userForm';

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main page',
      component: StudentsList
    },
    {
      path: '/login',
      name: 'Log in',
      component: UserForm,
      props: {
        type: 'Log in'
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: UserForm,
      props: {
        type: 'Register'
      }
    }
  ],
  mode: 'history'
});