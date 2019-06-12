<template>
  <div
    ref="ListHeader"
    id="ListHeader"
  >
    <b-row style="width: 100%">
      <b-col cols="9" md="6" class="col">
        <b-input-group>
          <b-form-input class="input-index" v-model="filterD" placeholder="按番号查找"></b-form-input>
          <b-input-group-append>
            <b-button class="btn-index" :disabled="!filterD" @click="filterD=''">
              清除
            </b-button>
          </b-input-group-append>
        </b-input-group>
        <b-input-group style="margin-top: 14px">
          <b-form-input class="input-index" v-model="filterN" placeholder="按演员查找"></b-form-input>
          <b-input-group-append>
            <b-button class="btn-index" :disabled="!filterN" @click="filterN=''">
              清除
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
      <b-col md="4" class="col" v-if="$store.state.isPC">
        <span style="color: #42b983">
          详情
        </span>
      </b-col>
      <b-col cols="3" md="2" class="col">
        <b-form-radio-group
          v-model="selected"
          buttons
          stacked
          size="sm"
        >
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value="0"
            button-variant="outline-primary"
            style="border-bottom: 0"
          >
            未收藏
          </b-form-radio>
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value=""
            button-variant="outline-primary"
            style="margin-top: 0"
          >
            全部
          </b-form-radio>
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value="1"
            button-variant="outline-primary"
          >
            已收藏
          </b-form-radio>
        </b-form-radio-group>
      </b-col>
    </b-row>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
export default {
  name: 'IndexHeader',
  data () {
    return {
      show: false,
      filterD: '',
      filterN: '',
      selected: ''
    }
  },
  computed: {
    filterAndSelected () {
      return {
        'designation': this.filterD,
        'starName': this.filterN,
        'isLike': this.selected
      }
    }
  },
  watch: {
    filterAndSelected () {
      this.$emit('fas-change', this.filterAndSelected)
    }
  }
}
</script>

<style scoped>
@import "ListHeader.css";
</style>
