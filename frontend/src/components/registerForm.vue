<template>
    <user-form :title=title :submit=onSubmit ></user-form>
</template>

<script>
    import UserForm from './userForm';

    export default {
        props: ['data'],
        name: 'RegisterForm',
        data: () => ({
            title: 'Register'
        }),
        components: {
            'user-form': UserForm
        },
        methods: {
            onSubmit(formValues) {
                debugger
                this.$http.post(API.login, formValues).then(
                    (response) => { debugger },
                    (error) => { debugger }
                )
            }
        }
    }
</script>