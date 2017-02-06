<template>
  <div class="user">
    <div>User: {{ $route.params.id }}</div>
    <p>
      <!-- use router-link component for navigation. -->
      <!-- specify the link by passing the `to` prop. -->
      <!-- <router-link> will be rendered as an `<a>` tag by default -->
      <router-link to="/user/tony/profile">Profile</router-link>
      <router-link to="/user/tony/posts">Posts</router-link>
    </p>
    <router-view></router-view>
</div>
</template>
<script>
    export default {
    }
</script>
