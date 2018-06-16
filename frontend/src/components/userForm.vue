<template>
    <v-flex class="user-form">
        <v-card class="user-form-card">
            <div class="user-form-baner">
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
import api from './../API';

export default {
    props:['type', 'setUser'],
    name: 'UserForm',
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
    methods:{
        onSubmit() {
            const { type, login, password, setToken } = this;

            this.$http.post(type === 'Log in' ? api.login : api.register, { login, password }).then(
                (response) => { 
                    const { body: { isSuccess, message, result  } } = response
                    if(isSuccess && typeof(result) === 'string')
                        setUser(result)
                    this.error = message;
                    return;
                },
                (error) => { 
                    this.error = 'global request or API error'; 
                    return; 
                }
            )
        }
    }
}
</script>

<style>
.user-form{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px auto;
}
.user-form-card{
    width: 400px;
    border-radius: 2px 2px 10px 10px;
	box-shadow: 5px 6px 18px -3px #777
}
.user-form-baner{
    background-color: #FEE140;
    background-image: linear-gradient(90deg, #FA709A 0%, #FEE140 100%);
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
