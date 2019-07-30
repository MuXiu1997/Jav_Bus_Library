import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
import { BRow, BCol, VBToggle } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/iconfont/iconfont.css'

import 'element-ui/lib/theme-chalk/index.css'

// noinspection JSUnusedGlobalSymbols
Vue.prototype.$axios = axios

Vue.component('b-row', BRow)
Vue.component('b-col', BCol)
Vue.directive('b-toggle', VBToggle)

Vue.config.productionTip = false

// noinspection JSUnusedGlobalSymbols
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
