<template>

  <div>
    <div :z-depth="1" class="top-bar">
      <mu-appbar style="width: 100%;" color="primary">
        <mu-button icon slot="left">
          <mu-icon value="menu"></mu-icon>
        </mu-button>
        标题
        <mu-menu slot="right">
          <mu-button flat to="login">登陆</mu-button>
        </mu-menu>
      </mu-appbar>
    </div>
    <mu-container v-bind:style="{marginTop:'60px',marginBottom:'60px'}">

      <mu-load-more>
        <slot></slot>
      </mu-load-more>

    </mu-container>
    <div style="position: fixed;bottom: 0;width: 100%">
      <mu-bottom-nav>
        <mu-bottom-nav-item title="首页" icon="home" to="/"></mu-bottom-nav-item>
        <mu-bottom-nav-item title="记账" icon="sentiment_satisfied_alt" to="bookkeep"></mu-bottom-nav-item>
        <mu-bottom-nav-item title="收藏" icon="favorite"></mu-bottom-nav-item>
        <mu-bottom-nav-item title="个人中心" icon="perm_identity" to="personal"></mu-bottom-nav-item>
      </mu-bottom-nav>
    </div>
  </div>


</template>

<script>
  export default {
    name: "Layout",
    data() {
      return {
        shift: 'movies'
      }
    }
  }

</script>

<style scoped>
  .top-bar {
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 999;
  }


</style>
