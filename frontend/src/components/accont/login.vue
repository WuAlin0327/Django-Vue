<template>
  <div style="margin-top: 30px">
    <p>{{login}}</p>
    <mu-alert color="error" delete v-if="alert" @delete="closeAlert()">
      <mu-icon left value="warning"></mu-icon>
      账号或者密码错误，请重试！
    </mu-alert>

    <mu-form ref="form" :model="validateForm" class="mu-demo-form">
      <mu-form-item label="用户名" prop="username" :rules="usernameRules">
        <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="密码" prop="password" :rules="passwordRules">
        <mu-text-field type="password" v-model="validateForm.password" prop="password"></mu-text-field>
      </mu-form-item>

      <mu-form-item>
        <mu-button color="primary" @click="submit">提交</mu-button>
        <mu-button @click="clear">重置</mu-button>
      </mu-form-item>
    </mu-form>
  </div>
</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        usernameRules: [
          {validate: (val) => !!val, message: '必须填写用户名'},
          {validate: (val) => val.length >= 3, message: '用户名长度大于3'}
        ],
        passwordRules: [
          {validate: (val) => !!val, message: '必须填写密码'},
          {validate: (val) => val.length >= 3 && val.length <= 10, message: '密码长度大于3小于10'}
        ],

        validateForm: {
          username: '',
          password: '',
          isAgree: false
        },
        alert: false
      }
    },
    props:['login'],
    methods: {
      submit() {
        this.$refs.form.validate()
          .then((result) => {
            var params = new URLSearchParams();
            params.append('username', this.$refs.form.model.username);
            params.append('password', this.$refs.form.model.password);
            this.$axios.post('/api/login/', params)
              .then(response => {
                if (response.data.alert) {
                  this.alert = true
                } else {
                  window.sessionStorage.setItem('isLogin', true);
                  window.sessionStorage.setItem('user', response.data.user);
                  window.sessionStorage.setItem('token', response.data.token);
                  window.location.href = '/'
                }
              });
          });
      },
      clear() {
        this.$refs.form.clear();
        this.validateForm = {
          username: '',
          password: '',
          isAgree: false
        };
      },
      closeAlert() {
        this.alert = false
      }
    },


  };

</script>

<style scoped>

</style>
