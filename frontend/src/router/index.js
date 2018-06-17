import Router from 'vue-router'

import StudentsList from '@/components/studentsList';
import UserForm from '@/components/userForm';
import ApiResult from '@/components/apiResult';

// import App from './../App';
// const { setUser, setStudents } = App.methods;

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: StudentsList,
      props: {
        //setStudents
      }
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
        //setUser
      }
    },
    {
      path: '/register',
      name: 'register',
      component: UserForm,
      props: {
        type: 'Register',
        //setUser
      }
    }
  ],
  mode: 'history'
});