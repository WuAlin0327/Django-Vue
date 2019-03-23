import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/comm/Index'
import Personal from '@/components/comm/PersonalCenter'
import Bookkeep from '@/components/Bookkeeping/Bookkeeping'
import Login from '@/components/accont/login'
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component:Index

    },
    {
      path:'/personal/',
      name:'personal',
      component:Personal
    },
    {
      path:'/bookkeep/',
      name:'bookkeep',
      component:Bookkeep
    },
    {
      path:"/login/",
      name:"login",
      component:Login
    }
  ]
})
