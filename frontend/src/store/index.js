import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  isLogin: false,
  UserName:'',
  token:'',

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
  getters
});

export default store
