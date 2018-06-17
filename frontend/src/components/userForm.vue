<template>
    <v-card class="app-card">
        <div class="app-card-header app-gradient">
            <h1 class="app-card-header-title">{{ type }}</h1>
            <p v-if=error class="app-card-header-subtitle">{{ error }}</p>
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
            if(to === 'Log out') {
                this.logout();
                return;
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
        },
        logout() {
            this.$store.commit('user', {});
            this.$router.push('/');
        }
    },
    created() {        
        if (this.user.token) {
            if(this.type === 'Log out') {
                this.logout();
                return;
            }
            this.$router.push('/');
        } 
    }
}
</script>