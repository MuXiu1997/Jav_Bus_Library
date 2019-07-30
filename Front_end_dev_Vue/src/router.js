import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  saveScrollPosition: true,
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'list',
      component: () => import(/* webpackChunkName: "list" */'./views/List.vue')
    },
    {
      path: '/:id',
      props: true,
      name: 'detail',
      component: () => import(/* webpackChunkName: "detail" */'./views/Detail.vue')
    }
  ]
})
