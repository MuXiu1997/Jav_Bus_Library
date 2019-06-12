import Vue from 'vue'
// import './plugins/axios'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'
// import VueLazyload from 'vue-lazyload'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/iconfont/iconfont.css'

import 'element-ui/lib/theme-chalk/index.css'
// import './plugins/element.js'

Vue.prototype.axios = axios

Vue.use(BootstrapVue)

// Vue.use(VueLazyload, {
//   preLoad: 1,
//   attempt: 2
// })

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
