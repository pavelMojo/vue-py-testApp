const root = 'http://localhost:8080';

export const procedures = {
    register: '/user',
    login:    '/login',
    logout:   '/logout',
    leave:    '/user',
    users:    '/users',
    user:     '/user',
    students: '/students',
    student:  '/student'
};

export const routs = {
    register: `${root}${procedures.register}`,
    login:    `${root}${procedures.login}`,
    logout:   `${root}${procedures.logout}`,
    leave:    `${root}${procedures.leave}`,
    users:    `${root}${procedures.users}`,
    user:     `${root}${procedures.user}`,
    students: `${root}${procedures.students}`,
    student:  `${root}${procedures.student}`
};

export default routs;