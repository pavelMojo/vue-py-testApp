<template>
    <v-flex class="user-form">
        <v-card class="user-form-card">
            <div class="user-form-baner gradient-background">
                <h1 class="user-form-title">{{ type }}</h1>
                <p v-if=error class="user-form-message">{{ error }}</p>
            </div>
            <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation >
                    
                    <v-text-field
                        v-model="login"
                        :rules="loginRules"
                        label="login"
                        required
                    ></v-text-field>
                    <v-text-field
                        v-model="password"
                        :rules="passwordRules"
                        label="password"
                        required
                    ></v-text-field>

                    <v-btn
                        :disabled="!valid || !login.length || !password.length"
                        @click="onSubmit"
                    >{{ type }}</v-btn>                    
                </v-form>
            </v-card-text>
        </v-card>
    </v-flex>
</template>

<script>
import api from './../api';

export default {
    name: 'UserForm',
    props: {
        type: String
    },
    watch: {
        'type' (to, from) {
            if(from !== to) {
                this.error = undefined
                this.login = ''
                this.password = ''
            } 
        }
    },
    data() {
        return {
            valid: true,
            error: undefined,
            login: '',
            loginRules: [
            v => !!v || 'Name is required',
            v => (v && v.length <= 30) || 'Name must be less than 30 characters'
            ],
            password: '',
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.length <= 30) || 'Password must be less than 30 characters'
            ],
        }   
    },
    computed:{
        user() {
            return this.$store.getters.user;
        }
    },
    methods:{
        onSubmit() {
            const { type, login, password, setUser } = this;
            this.$http.post(type === 'Log in' ? api.login : api.register, { login, password }).then(
                (response) => { 
                    const { body: { isSuccess, message, result  } } = response
                    if(isSuccess && typeof(result === 'object')) {
                        this.$store.commit('user', result)
                        this.$router.push(name='/');
                        return
                    }

                    this.error = message;
                    return;
                },
                (error) => { 
                    this.error = 'global request or API error'; 
                    return; 
                }
            )
        }
    },
    created() {
        const { token } = this.$store.getters.user;
        if (token) this.$router.push('/');
    }
}
</script>

<style>
.user-form{
    display: flex;
    justify-content: center;
    align-items: center;
}
.user-form-card{
    width: 400px;
    border-radius: 2px 2px 10px 10px;
	box-shadow: 4px 6px 20px -5px #777
}
.user-form-baner{
    display: flex;
    flex-direction: column;
}
.user-form-title{
    margin:16px;
    color: white;
}
.user-form-message{
    color: white;
    text-overflow: ellipsis;
}
</style>
