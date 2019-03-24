<template>
  <div>
    <mu-list>

      <mu-list-item button :ripple="false" v-if="isLogin">
        <mu-list-item-action>
          <mu-avatar :size="size">
            <img src="@/assets/grilfriend.png">
          </mu-avatar>
        </mu-list-item-action>
        <mu-list-item-title>{{username}}</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button :ripple="false" v-else>
        <mu-list-item-action>
          <mu-avatar :size="size">
            <img src="@/assets/匿名.png">
          </mu-avatar>
        </mu-list-item-action>

          <div>
            <mu-button color="primary" to="login">

            登陆
          </mu-button>
            <mu-button color="success" to="login">

            注册
          </mu-button>
          </div>

      </mu-list-item>

      <mu-list-item button :ripple="false">
        <mu-list-item-action>
          <mu-icon value="inbox"></mu-icon>
        </mu-list-item-action>
        <mu-list-item-title>功能</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button :ripple="false">
        <mu-list-item-action>
          <mu-icon value="grade"></mu-icon>
        </mu-list-item-action>
        <mu-list-item-title>功能</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button :ripple="false">
        <mu-list-item-action>
          <mu-icon value="send"></mu-icon>
        </mu-list-item-action>
        <mu-list-item-title>功能</mu-list-item-title>
      </mu-list-item>
      <mu-list-item button :ripple="false">
        <mu-list-item-action>
          <mu-icon value="drafts"></mu-icon>
        </mu-list-item-action>
        <mu-list-item-title>功能</mu-list-item-title>
      </mu-list-item>
    </mu-list>
  </div>

</template>

<script>
  export default {
    name: "PersonalContent",
    data() {
      return {
        size: 40,
        isLogin: this.$store.state.isLogin,
        username: this.$store.state.UserName,
      }
    },
    created() {

    }

  }
</script>

<style scoped>
  .demo-paper {

  }

</style>
