<template>
  <div>
    <transition name="fadeOutUp">
      <v-header
        v-show="$store.state.isPC || show"
        @filter-change="filterChange"
        id="ListHeader"/>
    </transition>
    <!--=============================================================================================================-->
    <v-main
      :videosData="videosDataSliced"
      :show="show"
      id="ListMain"/>
    <!--=============================================================================================================-->
    <!--toTop-->
    <span
      id="showHF"
      class="icon iconfont toTop"
      v-show="!$store.state.isPC"
      @click="show=!show">
    </span>
    <!--=============================================================================================================-->
    <transition name="fadeOutDown">
      <v-footer
        :currentPage="currentPage"
        :total="videosData.length"
        @current-change="currentChange"
        v-show="$store.state.isPC || show"/>
    </transition>
  </div>

</template>

<script>
import ListHeader from '../ListComponents/ListHeader.vue'
import ListMain from '../ListComponents/ListMain.vue'
import ListFooter from '../ListComponents/ListFooter.vue'

function manyIncludes (input, search) {
  if (!search) {
    return true
  }
  input = input.toLowerCase()
  search = search.toLowerCase()
  let keywords = search.split(' ')
  let result = true
  for (let keyword of keywords) {
    result = result && input.includes(keyword)
  }
  return result
}

function videoSort (thisOne, otherOne) {
  if (thisOne.pt > otherOne.pt) {
    return -1
  } else if (thisOne.pt < otherOne.pt) {
    return 1
  } else {
    if (thisOne.d > otherOne.d) {
      return 1
    } else if (thisOne.d < otherOne.d) {
      return -1
    } else {
      return 0
    }
  }
}
// noinspection JSUnusedGlobalSymbols
export default {
  components: {
    'v-header': ListHeader,
    'v-main': ListMain,
    'v-footer': ListFooter
  },
  name: 'List',
  data () {
    return {
      show: false,
      keepScrollTop: 0,

      filter: {
        designation: '',
        starName: '',
        isLike: ''
      },

      tableDataLength: null,
      currentPage: 1,
      initVideosData: [
        {
          d: null, // designation
          dt: null, // designation_title
          pt: null, // publish_time
          sn: null, // star_name
          mc: null, // magnet_count
          sc: null, // sample_count
          il: null // is_like
        }
      ]
    }
  },
  created () {
    this.getVideos()
  },
  computed: {
    videosData () {
      this.initCurrentPage()
      return this.initVideosData
        .filter((video) => {
          return manyIncludes(video.d, this.filter.designation)
        })
        .filter((video) => {
          return manyIncludes(video.sn, this.filter.starName)
        })
        .filter((video) => {
          return !this.filter.isLike || video.il === this.filter.isLike
        })
        .sort(videoSort)
    },
    videosDataSliced () {
      return this.videosData
        .slice((this.currentPage - 1) * 50, this.currentPage * 50)
    }

  },
  methods: {
    filterChange (obj) {
      this.filter = obj
    },
    currentChange (page) {
      this.currentPage = page
    },
    initCurrentPage () {
      this.currentPage = 1
    },
    getVideos () {
      this.$axios.get(`/api/videos/`)
        .then(response => {
          this.initVideosData = response.data
        })
    }
  }
}
</script>

<style scoped>
  @import "List.css";
</style>
