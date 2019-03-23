<template>
  <div>
    <mu-list>
    <mu-list-item button :ripple="false">
      <mu-list-item-action>
        <mu-avatar :size="size" s>
          <img src="@/assets/grilfriend.png">
        </mu-avatar>

      </mu-list-item-action>
      <mu-list-item-title>当前用户</mu-list-item-title>
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
        size: 40
      }
    },

  }
</script>

<style scoped>
  .demo-paper {

  }

</style>
