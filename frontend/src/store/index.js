import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  isLogin: window.sessionStorage.getItem('isLogin'),
  UserName:window.sessionStorage.getItem('user'),
  token:window.sessionStorage.getItem('token'),

};
const mutations = {
  Login(state){
    state.isLogin = !state.isLogin
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
