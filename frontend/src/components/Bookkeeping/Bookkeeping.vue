<template>
  <div>

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

  </div>
</template>

<script>
  export default {
    name: "Bookkeeping",
    data() {
      return {
        DataList: [],
        head: "",
        time_list: []
      }
    },
    created() {
      this.$axios.get('/api/charge/')
        .then(response => {
          this.DataList = response.data;
          for (var i in response.data) {
            if (this.time_list.includes(response.data[i].consume_date)) {

            } else {
              this.time_list.push(response.data[i].consume_date)
            }
          }


        })
    }
  }
</script>

<style scoped>

</style>
