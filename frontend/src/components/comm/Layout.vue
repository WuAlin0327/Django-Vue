<template>

  <div>
    <div :z-depth="1" class="top-bar">
      <mu-appbar style="width: 100%;" color="primary">
        <mu-button icon slot="left">
          <mu-icon value="menu"></mu-icon>
        </mu-button>
        待定
        <mu-menu slot="right" v-if="isLogin">
          <mu-button flat @click="openBotttomSheet">{{user}}</mu-button>
          <mu-bottom-sheet :open.sync="open">
            <mu-list>
              <mu-sub-header>请选择...</mu-sub-header>
              <mu-list-item button to="personal" @click="open=false">
                <mu-list-item-action>
                  <mu-icon value="perm_identity" color="green"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title>个人中心</mu-list-item-title>
              </mu-list-item>
              <mu-list-item button to="/" v-on:click="open=false">
                <mu-list-item-action>
                  <mu-icon value="inbox" color="blue"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title>首页</mu-list-item-title>
              </mu-list-item>
              <mu-list-item button @click="Logout">
                <mu-list-item-action>
                  <mu-icon value="remove_circle_outline" color="orange"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title>注销</mu-list-item-title>
              </mu-list-item>
              <mu-list-item button @click="open=false">
                <mu-list-item-action>
                  <mu-icon value="clear" color="red"></mu-icon>
                </mu-list-item-action>
                <mu-list-item-title>关闭</mu-list-item-title>
              </mu-list-item>
            </mu-list>
          </mu-bottom-sheet>
        </mu-menu>
        <mu-menu slot="right" v-else>
          <mu-button flat to="login">登陆</mu-button>
        </mu-menu>
      </mu-appbar>
    </div>
    <mu-container v-bind:style="{marginTop:'60px',marginBottom:'60px'}">

      <mu-load-more>
        <keep-alive v-bind:include="['Bookkeeping']">
          <slot></slot>
        </keep-alive>
      </mu-load-more>

    </mu-container>
    <div style="position: fixed;bottom: 0;width: 100%">
      <mu-bottom-nav>
        <mu-bottom-nav-item title="首页" icon="home" to="/"></mu-bottom-nav-item>
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
        shift: 'movies',
        isLogin: this.$store.getters.Login,
        user: this.$store.getters.User,
        open: false,

      }
    },
    methods: {
      Logout() {
        window.sessionStorage.clear();
        this.$store.state.isLogin = false;
        this.$store.state.UserName = '';
        this.$store.state.token = '';
        this.isLogin = false;
        window.location.href = '/';
        console.log('退出了')
      },
      openBotttomSheet() {
        this.open = true;
      },

    },


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
