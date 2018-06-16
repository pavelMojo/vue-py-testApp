<template>
    <user-form :title=title :submit=onSubmit ></user-form>
</template>

<script>
    import UserForm from './userForm';

    export default {
        props: ['data'],
        name: 'RegisterForm',
        data() {
            return {
                title: 'Login'
            }
        },
        components: {
            'user-form': UserForm
        },
        methods: {
            onSubmit(formValues) {
                debugger
                this.$http.post('http://localhost:8080/login', formValues).then(
                (response) => { debugger },
                (error) => { debugger }
            )}
        }
    }
</script>