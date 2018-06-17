import {  procedures, routs } from './'

export const testCalls = [
    {
        section:"POST",
    },
    {
        type: 'post',        
        name: procedures.login,
        path: routs.login,
        data: {
            login: "login",
            password: "password"
        }
    },
    {
        type: 'post',
        name: procedures.logout,
        path: routs.logout,
        data: {
            token: "69",
        }
    },
    {
        type: 'post',
        name: procedures.register,
        path: routs.register,
        data: {
            login: "unique login",
            password: "secret password"
        }
    },
    {
        type: 'post',
        name: procedures.student,
        path: routs.student,
        data: {
            name: "student name",
            info: "student info"
        }
    },
    {
        section:"GET",
        divider: 'divider-1'
    },
    {
        type: 'get',
        name: procedures.user,
        path: routs.user,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        type: 'get',
        name: procedures.users,
        path: routs.users,
        data: {
            token: "69",
        }
    },
    {
        type: 'get',
        name: procedures.student,
        path: routs.student,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        type: 'get',
        name: procedures.students,
        path: routs.students,
        data: {
            token: "69",
        }
    },
    {
        section:"DELETE",
        divider: 'divider-2'
    },
    {
        type: 'delete',
        name: procedures.user,
        path: routs.user,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        type: 'delete',
        name: procedures.student,
        path: routs.student,
        data: {
            token: "69",
            id: 0
        }
    }
];

export default testCalls;