<template>
    <div class="http-error">
        <span class="http-error__code app__gradient"> 404 </span>
        <p>Печалька...</p>
    </div>
</template>

<style lang="scss">
.http-error{
    &__code{
        font-size: 3000%;
        text-transform: uppercase;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
}
</style>
