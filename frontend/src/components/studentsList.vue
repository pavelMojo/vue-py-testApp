<template>
    <div>
        <h1>Main.vue</h1>
    </div>
</template>

<script>
export default {
    name: 'Main',    
    computed:{
        user() {
            return this.$store.getters.user;
        }
    },
    created() {
        if (!this.user.token) this.$router.push(name="login");
    }
}
</script>