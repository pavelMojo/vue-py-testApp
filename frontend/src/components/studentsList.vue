<template>
    <v-card class="app-card">
        <div class="app-card-header app-gradient">
            <h1 class="app-card-header-title">{{ title }}</h1>
            <p v-if=error class="app-card-header-subtitle">{{ error }}</p>
            <v-btn class="student-add-btn"
                absolute bottom right fab @click="addRecordsToStudents">
              <v-icon class="student-add-btn-icon" large >add</v-icon>
            </v-btn>
        </div>
        <v-card-text>
            <template v-for="(student, index) in students">
                <div class="student" :key="index">
                    <v-avatar :tile="true" :size="80" class="student-pic" >
                        <img :src="student.pic">
                    </v-avatar>
                    <v-list-tile-content>
                        <h2 v-html="student.name" class="student-name"></h2>
                        <p class="student-info" v-html="student.info"></p>
                    </v-list-tile-content>
                </div>
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
    methods:{
        addRecordsToStudents() {
            const { students } = this;        
            const generatedStudents = students.map((s, i) => ({
                id: s.id,
                name: `${s.name}.${i+1}`,
                info: s.info,
                pic: s.pic
            }));
            let newStudents = [];
            students.forEach((s, i) => { newStudents.push(s); newStudents.push(generatedStudents[i]) })

            this.$store.commit('students', newStudents);
            this.error = 'добавленные по клику записи были сгенерированы на клиенте. на сервере их нет';
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

<style lang="scss">
.student{
    display: flex;
    margin-bottom: 16px;
    &:last-child{
        margin-bottom: 0;
    }
    &-name{
        white-space: nowrap;
    }
    &-info{
    }
    &-pic{
        margin-right: 16px;
    }
    &-add-btn{
        &-icon{
            display: inline-flex !important;
            color: #FA709A !important;
        }
    }
}
// overwrite buildin style
.list__tile{
    padding: 0;
}
</style>