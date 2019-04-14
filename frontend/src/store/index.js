import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  isLogin: window.localStorage.getItem('isLogin'),
  UserName:window.localStorage.getItem('user'),
  token:window.localStorage.getItem('token'),

};
const mutations = {
  Login(state){
    state.isLogin = !state.isLogin
  },
  clear(state){
    state.isLogin = false;
    state.UserName = '';
    state.token = '';
  },
  login_sucess(state,data){
    console.log(data);
    state.isLogin = true;
    state.UserName = data.user;
    state.token = data.token
  }
};

const getters = {
  Login(state) {
    return state.isLogin
  },
  User(state){
    return state.UserName
  },
  Token(){
    return state.token
  }

};


const store = new Vuex.Store({
  state,
  getters,
  mutations
});

export default store
