<template>
  <div
    ref="ListMain"
    :class="{'isMobile':!$store.state.isPC && !show,'scrollStyle':true}"
    id="ListMain">
    <b-row v-for="(video,idx) of videosData"
           :key="idx"
           style="border-bottom: 1px solid rgba(66, 185, 131, 0.25);width: 100%;">
      <b-col cols="12" md="6" class="col" style="padding: 5px" @click="rowClick(video.d)">
        <el-img
          v-if="video.d"
          :src="`/images/${video.d}/${video.d}.jpg`"
          alt="" lazy :key="video.d"
          fit="contain"
          style="height: 400px;width: 100%">
          <div slot="placeholder"
               class="image-slot cover">
            加载中...
          </div>
        </el-img>
      </b-col>
      <b-col cols="8" md="4" style="text-align: left;margin: auto 0">
        <p>
          <b-badge class="badge-index">番号：</b-badge>
          {{video.d}}
        </p>
        <p>
          <b-badge class="badge-index">标题：</b-badge>
          {{video.dt}}
        </p>
        <p>
          <b-badge class="badge-index">演员：</b-badge>
          {{video.sn}}
        </p>
        <p>
          <b-badge class="badge-index">上市时间：</b-badge>
          {{video.pt}}
        </p>
      </b-col>
      <b-col cols="4" md="2" class="col" id="count-isLike">
        <p>
          <span>预览图：</span>
          <span v-if="video.sc==='0'" style="color: red">无</span>
          <span v-else style="color: #42b983">{{video.sc}}</span>
        </p>
        <p>
          <span>磁力链接：</span>
          <span v-if="video.mc==='0'" style="color: red">无</span>
          <span v-else style="color: #42b983">{{video.mc}}</span>
        </p>
        <span>收藏：</span>
        <b-checkbox
          :checked="video.il==='1'"
          switch
          class="switch-index"
          @change="(checked) => {isLikeChangeHandler(video, checked)}">
        </b-checkbox>
      </b-col>
    </b-row>
    <span
      class="icon iconfont toTop"
      :class="{'isMobile':!$store.state.isPC,'notShow':!show }"
      id="toTop"
      @click="scrollToTop"
      style="z-index: 999">
      </span>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
import { BBadge, BFormCheckbox } from 'bootstrap-vue'
import { Image } from 'element-ui'

export default {
  props: {
    videosData: {},
    show: {}
  },
  components: {
    'b-badge': BBadge,
    'b-checkbox': BFormCheckbox,
    'el-img': Image
  },
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
    videosData () {
      this.scrollToTop()
    }
  },
  methods: {
    scrollToTop () {
      let timer = null
      let el = this.$refs.ListMain
      cancelAnimationFrame(timer)
      timer = requestAnimationFrame(function fn () {
        let oTop = el.scrollTop
        if (oTop > 0) {
          el.scrollTop = oTop * 0.9
          timer = requestAnimationFrame(fn)
        } else {
          cancelAnimationFrame(timer)
        }
      })
    },
    rowClick (designation) {
      this.keepScrollTop = this.$refs.ListMain.scrollTop
      this.$router.push({ path: `/${designation}` })
    },
    isLikeChangeHandler (video, checked) {
      video.il = checked ? '1' : '0'
      this.$axios.put(`/api/videos/${video.d}`,
        { il: video.il }
      )
        .then()
    }
  }
}
</script>

<style scoped>
  @import "ListMain.css";
</style>
