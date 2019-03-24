<template>
  <div id="app">
    <Layout>
      <router-view/>
    </Layout>

  </div>
</template>

<script>
  import Layout from '@/components/comm/Layout'

  export default {
    name: 'App',
    components: {
      Layout
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*text-align: center;*/
    color: #2c3e50;

  }

  * {
    padding: 0;
    margin: 0;
  }

  a {
    text-decoration: none;
    color: #000;
  }

  ul {
    list-style: none;

  }

</style>
