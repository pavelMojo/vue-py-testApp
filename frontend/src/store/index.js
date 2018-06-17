import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        user: {},
        students: []
    },
    getters: {
        user(state) {
            return state.user
        },
        students(state) {
            return state.students
        }
    },
    mutations: {
        user(state, user) {
            state.user = user;
        },
        students(state, students) {
            state.students = students
        }
    }
});

export default store;