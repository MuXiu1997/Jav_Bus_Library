<template>
  <div ref="ListFooter"
       id="ListFooter"
  >
    <div style="width: 100%">
      <b-row style="width: 100%">
        <b-col>
          <el-pagination
            @current-change="currentChange"
            :current-page="currentPage"
            :page-size="50"
            :layout="parameter.layout"
            :pager-count="parameter.count"
            :total="tableDataLength"
            style="margin: 0 auto;text-align: center"
          >
          </el-pagination>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
import { Pagination } from 'element-ui'
export default {
  components: { 'el-pagination': Pagination },
  props: ['currentPage', 'tableDataLength'],
  name: 'ListFooter',
  computed: {
    parameter () {
      if (this.$store.state.isPC) {
        return {
          layout: 'total, prev, pager, next, jumper',
          count: 7
        }
      } else {
        return {
          layout: 'prev, pager, next',
          count: 5
        }
      }
    }
  },
  methods: {
    currentChange (page) {
      this.$emit('current-change', page)
    }
  }
}
</script>

<style scoped>
@import "ListFooter.css";
</style>
