<template>
  <div
    ref="ListMain"
    :class="{'isMobile':!$store.state.isPC && !show,'scrollStyle':true}"
    id="ListMain"
  >
    <b-row v-for="(data,idx) of tableData"
           :key="idx"
           style="border-bottom: 1px solid rgba(66, 185, 131, 0.25);width: 100%;"
    >
      <b-col cols="12" md="6" class="col" style="padding: 5px" @click="rowClick(data.designation)">
        <el-img :src="data.cover" alt="" lazy :key="data.cover" fit="contain" style="height: 400px;width: 100%">
          <div slot="placeholder"
               class="image-slot"
               style=
                 "background-color: rgba(0,0,0,0);
                 color: #42b983;
                 line-height: 400px;
                 height: 100px;
                 width: 100%;
                 text-align: center"
          >
            加载中...
          </div>
        </el-img>
      </b-col>
      <b-col cols="8" md="4" style="text-align: left;margin: auto 0">
        <p>
          <b-badge class="badge-index">番号：</b-badge>
          {{data.designation}}
        </p>
        <p>
          <b-badge class="badge-index">标题：</b-badge>
          {{data.designationTitle}}
        </p>
        <p>
          <b-badge class="badge-index">演员：</b-badge>
          {{data.starName}}
        </p>
        <p>
          <b-badge class="badge-index">上市时间：</b-badge>
          {{data.publishTime}}
        </p>
      </b-col>
      <b-col cols="4" md="2" class="col" id="count-isLike">
        <p>
          <span>预览图：</span>
          <span v-if="!data.sampleCount" style="color: red">无</span>
          <span v-if="data.sampleCount" style="color: #42b983">{{data.sampleCount}}</span>
        </p>
        <p>
          <span>磁力链接：</span>
          <span v-if="!data.magnetCount" style="color: red">无</span>
          <span v-if="data.magnetCount" style="color: #42b983">{{data.magnetCount}}</span>
        </p>
        <span>收藏：</span>
        <b-checkbox v-model="data.isLike" switch class="switch-index">
        </b-checkbox>
      </b-col>
    </b-row>
    <span
      class="icon iconfont toTop"
      :class="{'isMobile':!$store.state.isPC,'notShow':!show }"
      id="toTop"
      @click="scrollToTop"
      style="z-index: 999"
    >
      </span>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
import { Image } from 'element-ui'

export default {
  props: ['tableData', 'show'],
  components: { 'el-img': Image },
  name: 'ListMain',
  data () {
    return {
      keepScrollTop: 0
    }
  },
  activated () {
    let timer = setInterval(() => {
      if (this.$refs.ListMain.scrollTop !== this.keepScrollTop) {
        this.$refs.ListMain.scrollTop = this.keepScrollTop
      } else {
        clearInterval(timer)
      }
    })
  },
  watch: {
    tableData () {
      this.scrollToTop()
    }
  },
  methods: {
    scrollToTop () {
      this.$refs.ListMain.scrollTop = 0
    },
    rowClick (designation) {
      this.keepScrollTop = this.$refs.ListMain.scrollTop
      this.$router.push({ path: '/info/' + designation })
    }
  }
}
</script>

<style scoped>
  @import "ListMain.css";
</style>
