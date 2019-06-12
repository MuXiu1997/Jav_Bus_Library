import Vue from 'vue'
import Router from 'vue-router'
import List from './views/List'

Vue.use(Router)

export default new Router({
  saveScrollPosition: true,
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'list',
      component: List
    },
    {
      path: '/info/:id',
      props: true,
      name: 'info',
      component: () => import(/* webpackChunkName: "Info" */'./views/Info.vue')
    }
  ]
})
