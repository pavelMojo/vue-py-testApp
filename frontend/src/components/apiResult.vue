<template>
    <pre class='api-result'>
        {{ requestJson }}
    </pre>
</template>

<script>
export default {
    props:['apiCallResult'],
    name: 'apiCall',
    watch: {
        'apiCallResult' (to, from) {
            if(from !== to) this.requestJson = ''
        }
    },
    data() {
        return({
            requestJson: 'API not call yet. \n\tChoose any option from "TEST API CALL" menu on top'
        });
    },
    created() {
        const { apiCallResult } = this;
        if (!apiCallResult) return;
        
        // forbid manual transition to this page. Not necessary
        // if (apiCallResult === undefined) this.$router.push(name='/');

        const excludeBodyText = (key, value) =>
            (typeof value === 'string' && key === 'bodyText') ? 
                undefined : value 
        
        this.requestJson = JSON.stringify(apiCallResult, excludeBodyText, 2);
    }
}
</script>

<style>
.api-result{
    padding-left: 30px;
    text-align: start;
}
</style>