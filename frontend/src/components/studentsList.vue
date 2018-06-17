<template>
    <v-card class="app-card">
        <div class="app-card-header app-gradient">
            <h1 class="app-card-header-title">{{ title }}</h1>
            <p v-if=error class="app-card-header-subtitle">{{ error }}</p>
        </div>
        <v-card-text>
            <template v-for="(student, index) in students">
                <p :key="index">{{ student.info}}</p>
            </template>
        </v-card-text>
    </v-card>
</template>

<script>
import api from './../api';

export default {
    name: 'Main',
    data() {
        return {
            title: 'Students list:',
            error: ''
        }
    },
    computed:{
        user() {
            return this.$store.getters.user;
        },
        students() {
            return this.$store.getters.students; 
        }
    },
    created() {
        const { token } = this.user;
        if (token) {
            this.$http.get(`${api.students}/token="${token}"&`).then(
                (response) => { 
                    const { body: { isSuccess, message, result  } } = response
                    if (isSuccess && typeof(result === 'array')) {
                        this.$store.commit('students', result)
                        return
                    }
                    this.error = message;
                    return;
                },
                (error) => { 
                    this.error = 'global request or API error';
                }
            )
        }
        else this.$router.push(name="login");
    }
}
</script>