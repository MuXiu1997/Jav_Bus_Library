<template>
  <div id="infoHeader">
    <div
      v-b-toggle.accordion="true"
      @click="show=!show"
      id="title"
    >
      <span style="font-size: 16px;color: #42b983">磁 力 链 接 Magnet Links</span>
      <i class=" header-icon el-icon-paperclip" style="font-size: 16px;color: #42b983"></i>
    </div>
    <b-collapse
      id="accordion"
      ref="accordion"
      class="scrollStyle"
    >
      <b-table
        hover
        :items="magnetTableData"
        :fields="fields"
        @row-dblclicked="magnetDblclick"
        id="magnetTable"
      >
      </b-table>
    </b-collapse>
    <div
      v-viewer="{url: 'data-large', navbar: false, movable: false, title: false, rotatable: false, scalable:false}"
      style="position: fixed;top: 45px;right: 0;bottom: 0;left: 0;overflow: auto;z-index: 1"
      class="scrollStyle"
    >
      <img
        v-for="url in urlList"
        :key="url"
        style="width: 50%;display: block;margin:20px auto;"
        :src="url" alt="">
    </div>
    <span
      class="icon iconfont toTop"
      id="back"
      @click="back"
    >
    </span>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
import 'viewerjs/dist/viewer.css'
import 'v-viewer'

export default {
  name: 'Info',
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
      magnetTableData: [],
      urlList: [],
      designation: this.$route.params.id
    }
  },
  created () {
    this.getInfoData()
  },
  methods: {
    getInfoData () {
      this.axios.get('/api/GET/infos/', {
        params: {
          designation: this.designation
        }
      })
        .then(response => {
          this.magnetTableData = response.data.magnetTableData
          this.urlList = response.data.urlList
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
  @import "Info.css";
</style>
