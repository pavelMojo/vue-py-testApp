<template>
    <pre class='api__result'>
        {{ requestJson }}
    </pre>
</template>

<script>
export default {
    props:['apiCallResult'],
    name: 'apiResult',
    watch: {
        'apiCallResult' (to, from) {
            debugger
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
        
        const excludeBodyText = (key, value) =>
            (typeof value === 'string' && key === 'bodyText') ? 
                undefined : value 
        
        this.requestJson = JSON.stringify(apiCallResult, excludeBodyText, 2);
    }
}
</script>

<style lang="scss">
.api{
    &__result{
    text-align: start;
    overflow: auto;
    margin: 0 auto auto 0;
    padding: 24px;
}
}
</style>