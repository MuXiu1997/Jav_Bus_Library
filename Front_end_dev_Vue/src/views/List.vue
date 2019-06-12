<template>
  <div>
    <transition name="fadeOutUp">
      <v-header
        v-show="$store.state.isPC || show"
        @fas-change="FASChange"
        id="ListHeader"
      />
    </transition>
    <!--=============================================================================================================-->
    <v-main
      :tableData="tableData"
      :show="show"
      id="ListMain"
    />
    <!--=============================================================================================================-->
    <span
      id="showHF"
      :class="{'hide':$store.state.isPC,'icon iconfont toTop':true}"
      @click="show=!show"
    >
    </span>
    <!--=============================================================================================================-->
    <transition name="fadeOutDown">
      <v-footer
        :currentPage="currentPage"
        :tableDataLength="tableDataLength"
        @current-change="currentChange"
        v-show="$store.state.isPC || show"
      />
    </transition>
  </div>

</template>

<script>
export default {
  components: {
    'v-header': () => import(/* webpackChunkName: "List" */'../ListComponents/ListHeader.vue'),
    'v-main': () => import(/* webpackChunkName: "List" */'../ListComponents/ListMain.vue'),
    'v-footer': () => import(/* webpackChunkName: "List" */'../ListComponents/ListFooter.vue')
  },
  name: 'List',
  data () {
    return {
      show: false,
      keepScrollTop: 0,

      FAS: {
        designation: '',
        starName: '',
        isLike: ''
      },

      tableDataLength: null,
      currentPage: 1,
      tableData: [
        {
          cover: null,
          designation: null,
          designationTitle: null,
          starName: null,
          publishTime: null,
          sampleCount: null,
          magnetCount: null,
          isLike: null
        }
      ]
    }
  },
  created () {
    this.getTableData()
  },
  methods: {
    FASChange (obj) {
      this.FAS = obj
      this.getTableData()
    },
    currentChange (page) {
      this.getTableData(page)
    },
    // switchIsLike (rowData) {
    //   this.axios.patch('/api/PATCH/table-data/is-like', {
    //     'designation': rowData.designation,
    //     'isLike': !rowData.isLike
    //   })
    // },
    getTableData (page) {
      this.axios.get('/api/GET/table-data', {
        params: {
          designation: this.FAS['designation'],
          starName: this.FAS['starName'],
          isLike: this.FAS['isLike'],
          currentPage: page || 1
        }
      })
        .then(response => {
          this.tableData = response.data['tableData']
          this.tableDataLength = response.data['len']
          this.currentPage = response.data['currentPage']
        })
    }
  }
}
</script>

<style scoped>
  @import "List.css";
</style>
