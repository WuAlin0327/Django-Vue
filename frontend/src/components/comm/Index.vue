<template>
  <mu-row gutter v-bind:style="{marginTop:''}">


    <mu-col span="4">
      <div class="grid-content">
        <router-link to="bookkeep">
          <img src="@/assets/钱袋.png" alt="" width="60" height="60">
          <p>记账</p>
        </router-link>
      </div>
    </mu-col>

    <mu-col span="4">
      <div class="grid-content">
        <img src="@/assets/书.png" alt="" width="60" height="60">
        <p>读书</p>
      </div>
    </mu-col>
    <mu-col span="4">
      <div class="grid-content">
        <img src="@/assets/备忘录.png" alt="" width="60" height="60">
        <p>备忘录</p>
      </div>
    </mu-col>
    <mu-col span="4">
      <div class="grid-content">
        <img src="@/assets/blog.png" alt="" width="60" height="60">
        <p>博客</p>
      </div>
    </mu-col>

  </mu-row>
</template>

<script>
  export default {
    name: "Index"
  }
</script>

<style scoped>
  .grid-cell {
    /*padding: 20px 5px;*/
    /*height: 150px;*/

  }

  .grid-content {
    text-align: center;
    padding-top: 25px;
  }
  a{
    color: #000;
  }

</style>
