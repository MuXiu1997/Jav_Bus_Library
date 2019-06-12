import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isPC: null
  },
  mutations: {
    handleIsPC (state, isPC) {
      state.isPC = isPC
    }
  },
  actions: {
    handleIsPC (context, isPC) {
      context.commit('handleIsPC', isPC)
      console.log(123)
    }
  }
})
