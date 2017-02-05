<!-- Top Nav bar -->
<template>
<nav id="topbar" class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container center-block">
    <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
            <li><a class="navbar-brand" href="#">Dashboad</a></li>
            <li><a href="http://10.20.60.21:8080/job/WKD/job/WKD_API_Test/">微客多</a></li>
            <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Test <b class="caret"></b></a>
            <ul class="dropdown-menu">
                    <li><a href="#">admin</a></li>
                    <li><a href="#">ModTest</a></li>
            </ul>
            </li>
            <li><a href="/demo">Demo</a></li>
            <li><a href="/erp">WMS</a></li>
            <li><a href="#">{{ info }}</a></li>
        </ul>

        <ul id="nav_right" class="nav navbar-nav navbar-right">

            <li v-if="show" class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Account
                    <img src="/static/me.ico" with="20" height="20">
                    <b class="caret"></b></a>
                <ul class="dropdown-menu">
                    <li><a href="#">MyInfo</a></li>
                    <li><a href="#">Change Password</a></li>
                    <li><a href="#">Change Email</a></li>
                </ul>
            </li>
            <li><a href="#">Logout</a></li>

            <li><a href="/login">Login</a></li>

        </ul>
    </div>
    </div>
</nav>
<template>


<script>
export default {
  name: 'nav',
  data () {
    return {
      info: 'SCTek Test Management',
      show: true
    }
  }
}
</script>

<style>
/* style */
</style>
