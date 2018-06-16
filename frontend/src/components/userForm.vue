<template>
    <v-flex class="user-form">
        <v-card class="user-form-card">
                <div class="user-form-baner">
                    <h1 class="user-form-title">{{ title }}</h1>
                    <p class="user-form-title">{{ error }}</p>
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
                            class="user-form-submit-btn"
                            :disabled="!valid"
                            @click="onSubmit"
                        >submit</v-btn>
                    </v-form>
                </v-card-text>
        </v-card>
    </v-flex>
</template>

<script>
export default {
    props:['title', 'submit'],
    name: 'UserForm',    
    data() {
        return {
            valid: true,
            error: 'error mock',
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
        onSubmit(e) {
            e.preventDefault();
            const { login, password } = this;
            this.submit({ login, password })
        }
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
	box-shadow: 5px 6px 18px -3px #777
}
.user-form-baner{
    height: 80px;
    background-color: #FEE140;
    background-image: linear-gradient(90deg, #FA709A 0%, #FEE140 100%);
    display: flex;
    justify-content: space-around;
    align-items: center;
}
.user-form-title{
    color: white;
}
</style>
