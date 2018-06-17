import {  procedures, pathes } from './'

export const testCalls = [
    {
        section:"POST",
    },
    {
        type: 'post',
        name: procedures.register,
        path: pathes.register,
        data: {
            login: "unic login",
            password: "sicret password"
        }
    },
    {
        type: 'post',        
        name: procedures.login,
        path: pathes.login,
        data: {
            login: "unic login",
            password: "sicret password"
        }
    },
    {
        type: 'post',
        name: procedures.logout,
        path: pathes.logout,
        data: {
            token: "69",
        }
    },
    {
        type: 'post',
        name: procedures.student,
        path: pathes.student,
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
        name: procedures.users,
        path: pathes.users,
        data: {
            token: "69",
        }
    },
    {
        type: 'get',
        name: procedures.user,
        path: pathes.user,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        type: 'get',
        name: procedures.students,
        path: pathes.students,
        data: {
            token: "69",
        }
    },
    {
        type: 'get',
        name: procedures.student,
        path: pathes.student,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        section:"DELETE",
        divider: 'divider-2'
    },
    {
        type: 'delete',
        name: procedures.leave,
        path: pathes.leave,
        data: {
            token: "69",
        }
    },
    {
        type: 'delete',
        name: procedures.user,
        path: pathes.user,
        data: {
            token: "69",
            id: 0
        }
    },
    {
        type: 'delete',
        name: procedures.student,
        path: pathes.student,
        data: {
            token: "69",
            id: 0
        }
    }
];

export default testCalls;