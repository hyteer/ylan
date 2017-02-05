<template>
<div class="container">  
  <div class="home">
    <h3>{{ msg }}</h3>
    <h2>WKD Test</h2>
  </div>

  <div id="main_container" class="container">
    <h3>YLanTek Admin</h3>
    Tools&amp;Demos for testing.
  </div>
</div>
  <!-- /.container -->
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'SCTek Test Management'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
