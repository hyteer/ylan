<template>
  <div class="elbutton">
      <h3>ElementUI Button</h3>
      <div class="block">
        <span class="demonstration">默认显示颜色</span>
        <span class="wrapper">
          <el-button type="success">成功按钮</el-button>
          <el-button type="warning">警告按钮</el-button>
          <el-button type="danger">危险按钮</el-button>
          <el-button type="info">信息按钮</el-button>
        </span>
      </div>
      <div class="block">
        <span class="demonstration">hover 显示颜色</span>
        <span class="wrapper">
          <el-button :plain="true" type="success">成功按钮</el-button>
          <el-button :plain="true" type="warning">警告按钮</el-button>
          <el-button :plain="true" type="danger">危险按钮</el-button>
          <el-button :plain="true" type="info">信息按钮</el-button>
        </span>
      </div>

      <h3>Element Group</h3>
      <el-button type="primary" icon="edit"></el-button>
      <el-button type="primary" icon="share"></el-button>
      <el-button type="primary" icon="delete"></el-button>
      <el-button type="primary" icon="search">搜索</el-button>
      <el-button type="primary">上传<i class="el-icon-upload el-icon--right"></i></el-button>
  </div>
</template>

<script>
  export default{}
</script>

<style scoped>
.block{margin:20px 15px;}


</style>
