<template>
<div class="elementui">
  <el-row>
  <el-col :span="24"><div class="grid-content bg-purple-dark">
    <h2>ElementUI Demo</h3>
    <p>
      <!-- use router-link component for navigation. -->
      <!-- specify the link by passing the `to` prop. -->
      <!-- <router-link> will be rendered as an `<a>` tag by default -->
      <router-link to="/element/grid">Grid</router-link>
      <router-link to="/element/menu">Menu</router-link>
      <router-link to="/element/button">Button</router-link>
      <router-link to="/element/form">Form</router-link>
    </p>
    <router-view></router-view>
  </div></el-col>
</el-row>

</div>
</template>

<script>
    export default {
    }
</script>
