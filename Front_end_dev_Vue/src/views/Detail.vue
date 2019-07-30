<template>
  <div id="infoHeader">
    <div
      v-b-toggle.accordion="true"
      @click="show=!show"
      id="title">
      <span style="font-size: 16px;color: #42b983">磁 力 链 接 Magnet Links</span>
      <i class=" header-icon el-icon-paperclip" style="font-size: 16px;color: #42b983"></i>
    </div>
    <b-collapse
      id="accordion"
      ref="accordion"
      class="scrollStyle">
      <b-table
        hover
        :items="magnets"
        :fields="fields"
        @row-dblclicked="magnetDblclick"
        id="magnetTable">
      </b-table>
    </b-collapse>

    <div
      style="position: fixed;top: 45px;right: 0;bottom: 0;left: 0;overflow: auto;z-index: 1"
      class="scrollStyle"
      ref="samples">
      <img
        v-for="sample in samples"
        :key="sample"
        style="width: 50%;display: block;margin:20px auto;"
        :src="`/images/${designation}/${sample}`"
        alt=""/>
    </div>
    <span
      class="icon iconfont toTop"
      id="back"
      @click="back">
    </span>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
import Viewer from 'viewerjs'
import 'viewerjs/dist/viewer.css'
import { BCollapse, BTable } from 'bootstrap-vue'
export default {
  name: 'Detail',
  components: {
    'b-collapse': BCollapse,
    'b-table': BTable
  },
  data () {
    return {
      show: true,
      fields: {
        Name: {
          key: 'name',
          label: '文件名',
          tdClass: 'col1'
        },
        Size: {
          key: 'size',
          label: '大小',
          tdClass: 'col2'

        },
        Time: {
          key: 'time',
          label: '日期',
          tdClass: 'col3'
        }
      },
      magnets: [],
      samples: [],
      designation: this.$route.params.id,
      viewer: null
    }
  },
  created () {
    this.getInfoData()
    this.$nextTick(() => {
      this.viewer = new Viewer(this.$refs['samples'], {
        title: 0,
        fullscreen: false,
        navbar: 0,
        toolbar: {
          prev: true,
          zoomIn: true,
          reset: true,
          zoomOut: true,
          rotateLeft: true,
          rotateRight: true,
          next: true
        }
      })
    })
  },
  methods: {
    getInfoData () {
      this.$axios.get(`/api/videos/${this.designation}/details/`, {
        params: {
          designation: this.designation
        }
      })
        .then(response => {
          // noinspection JSUnresolvedVariable
          this.magnets = response.data.mi
          this.samples = response.data.sl
          this.$nextTick(() => {
            this.viewer.update()
          })
        })
    },
    magnetDblclick (row) {
      window.open(row.link, '_self')
    },
    back () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
  @import "Detail.css";
</style>
