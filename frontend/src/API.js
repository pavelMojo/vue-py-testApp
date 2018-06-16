const root = 'http://localhost:8080';

export const procedures = {
    register: '/register',
    login:    '/login',
    logout:   '/logout',
    leave:    '/leave',
    students: '/students',
    student:  '/student'
};

export const pathes = {
    register: `${root}${procedures.register}`,
    login:    `${root}${procedures.login}`,
    logout:   `${root}${procedures.logout}`,
    leave:    `${root}${procedures.leave}`,
    students: `${root}${procedures.students}`,
    student:  `${root}${procedures.student}`
};

export const calls = [
    {
        name: procedures.register,
        path: pathes.register,
        data: {
            login: "unic login",
            password: "sicret password"
        }
    },
    {
        name: procedures.login,
        path: pathes.login,
        data: {
            login: "unic login",
            password: "sicret password"
        }
    },
    {
        name: procedures.logout,
        path: pathes.logout,
        data: {
            token: "69",
        }
    },
    {
        name: procedures.leave,
        path: pathes.leave,
        data: {
            token: "69",
        }
    }
]

export default pathes;