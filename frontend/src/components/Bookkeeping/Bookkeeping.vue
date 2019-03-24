<template>
  <div>


    <mu-paper :z-depth="5">

      <div class="statistical">
        <ul>
          <li><p>本月结余：</p>
            <p style="font-size: 25px">{{income-outlay}}元</p></li>
          <li><p>总收入：</p>
            <p style="font-size: 20px">{{income}}元</p></li>
          <li>
            <p>总支出：</p>
            <p style="font-size: 20px">{{outlay}}元</p>
          </li>
        </ul>
      </div>

    </mu-paper>

    <div style="margin-top: 5px">
      <mu-button small color="teal" @click="openFullscreenDialog">
        <mu-icon value="add"></mu-icon>
        记一笔
      </mu-button>
    </div>

    <mu-list textline="two-line">
      <div v-for="(time,index) in time_list">
        <mu-sub-header>{{time}}</mu-sub-header>
        <div v-for="(item,index) in DataList">
          <div v-if="time===item.consume_date">
            <mu-list-item avatar button :ripple="false">
              <mu-list-item-action>
                <mu-avatar>
                  <mu-icon :value="item.consume_icon"></mu-icon>
                </mu-avatar>
              </mu-list-item-action>
              <mu-list-item-content>
                <mu-list-item-title>{{item.consume_title}} <span style="float: right">{{item.consume_date}}</span>
                </mu-list-item-title>
                <mu-list-item-sub-title>
                  {{item.income_or_outlay}}: <span>{{item.doughy}}元</span>
                </mu-list-item-sub-title>
              </mu-list-item-content>
            </mu-list-item>

          </div>
        </div>
      </div>
    </mu-list>
    <div>
      <mu-dialog width="100%" transition="slide-bottom" fullscreen :open.sync="openFullscreen">
        <mu-appbar color="primary" title="记一笔">
          <mu-button slot="left" icon @click="closeFullscreenDialog">
            <mu-icon value="close"></mu-icon>
          </mu-button>
          <mu-button slot="right" flat @click="AddBookkeeping">
            添加
          </mu-button>
        </mu-appbar>
        <mu-form :model="form">
          <mu-form-item prop="input" label="金额：" :style="{padding:'5px'}">
            <mu-text-field v-model="form.input"></mu-text-field>
          </mu-form-item>
        </mu-form>
        <mu-tabs :value.sync="active" inverse color="secondary" text-color="rgba(0, 0, 0, .54)" center>
          <mu-tab>支出</mu-tab>
          <mu-tab>收入</mu-tab>
        </mu-tabs>
        <div style="padding: 24px;" v-if="active === 0">
          <ul class="check_ul">
            <li v-for="(item,index) in check_list" :key="index" v-if="item.income_or_outlay === 1">
              <mu-flex class="select-control-row">
                <mu-radio v-model="form.radio" :value="item.id" :uncheck-icon="item.icon" checked-icon="done"
                          :label="item.title"></mu-radio>
              </mu-flex>
            </li>
          </ul>
        </div>
        <div style="padding: 24px;" v-if="active === 1">
          <ul class="check_ul">
            <li v-for="(item,index) in check_list" :key="index" v-if="item.income_or_outlay === 2">
              <mu-flex class="select-control-row">
                <mu-radio v-model="form.radio" :value="item.id" :uncheck-icon="item.icon" checked-icon="done"
                          :label="item.title"></mu-radio>
              </mu-flex>
            </li>
          </ul>
        </div>
      </mu-dialog>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Bookkeeping",
    data() {
      return {
        DataList: [],
        head: "",
        time_list: [],
        income: 0, //收入
        outlay: 0,//支出
        openFullscreen: false,
        check_list: [],
        active: 0,
        form: {
          radio: 1,
          input: '',
        }

      }
    },
    created() {
      // var params = new URLSearchParams;
      var token = this.$store.state.token;
      var isLogin = this.$store.getters.Login;
      if (isLogin) {
        this.$axios.get('/api/charge/?token=' + token)
          .then(response => {
            this.DataList = response.data;
            for (var i in response.data) {
              if (this.time_list.includes(response.data[i].consume_date)) {

              } else {
                this.time_list.push(response.data[i].consume_date)
              }

              var classes = response.data[i].income_or_outlay;
              var doughy = response.data[i].doughy;
              if (classes == '收入') {
                this.income += doughy
              } else {
                this.outlay += doughy
              }

            }
          })
      } else {
        alert('请先登陆！');
        this.$router.push('/login/')
      }
    },
    methods: {
      openFullscreenDialog() {
        this.openFullscreen = true;
        this.$axios.get('/api/consu_type/')
          .then(response => {
            this.check_list = response.data
          })
      },
      AddBookkeeping() {
        const token = this.$store.state.token;
        const isLogin = this.$store.getters.Login;

        if (isLogin) {
          var params = new URLSearchParams;
          params.append('ofconsumption_id', this.form.radio);
          params.append('doughy', this.form.input);
          this.$axios.post('/api/charge/?token=' + token, params)
            .then(response => {
              const status = JSON.parse(response.data.status);
              if (status) {
                this.income = 0;
                this.outlay = 0;
                this.DataList = [];
                this.time_list = [];
                //获取最新的数据
                this.$axios.get('/api/charge/?token=' + token)
                  .then(response => {
                    this.DataList = response.data;
                    for (var i in response.data) {
                      if (this.time_list.includes(response.data[i].consume_date)) {

                      } else {
                        this.time_list.push(response.data[i].consume_date)
                      }

                      var classes = response.data[i].income_or_outlay;
                      var doughy = response.data[i].doughy;
                      if (classes == '收入') {
                        this.income += doughy
                      } else {
                        this.outlay += doughy
                      }

                    }
                  })
              } else {
                alert('添加失败')
              }
            })
        }
        this.openFullscreen = false;
      },
      closeFullscreenDialog() {
        this.openFullscreen = false;
        console.log(this.DataList);
        console.log(this.check_list);
        this.DataList = []
      },

    },
    watch: {
      Datalist() {
        console.log('这个值改变了')
      }
    }
  }
</script>

<style scoped>
  .statistical {
    background-color: #757575;
    height: 115px;
    width: 100%;
    padding: 10px;
  }

  .statistical li p {
    color: #fafafa;
    font-size: 16px;
  }

  .statistical li {
    float: left;
    margin-right: 20px;
  }

  .check_ul li {
    float: left;
    width: 33%;
    padding: 20px;
    margin-top: 10px;
  }


</style>
