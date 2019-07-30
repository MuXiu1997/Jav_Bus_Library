<template>
  <div id="app">
    <keep-alive include="List">
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: 'app',
  created () {
    window.onresize = () => {
      return this.$store.dispatch('handleIsPC', `${document.documentElement.clientWidth}` >= 768)
    }
    this.$store.dispatch('handleIsPC', `${document.documentElement.clientWidth}` >= 768)
      .then()
  }
}
</script>
<style>
  @import "App.css";
</style>
