<template>
  <div
    ref="ListHeader"
    id="ListHeader"
  >
    <b-row style="width: 100%">
      <b-col cols="9" md="6" class="col">
        <b-input-group>
          <b-form-input class="input-index" v-model="filter.designation" placeholder="按番号查找"></b-form-input>
          <b-input-group-append>
            <b-button class="btn-index" :disabled="!filter.designation" @click="filter.designation=''">
              清除
            </b-button>
          </b-input-group-append>
        </b-input-group>
        <b-input-group style="margin-top: 14px">
          <b-form-input class="input-index" v-model="filter.starName" placeholder="按演员查找"></b-form-input>
          <b-input-group-append>
            <b-button class="btn-index" :disabled="!filter.starName" @click="filter.starName=''">
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
          v-model="filter.isLike"
          buttons
          stacked
          size="sm">
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value="0"
            button-variant="outline-primary"
            style="border-bottom: 0">
            未收藏
          </b-form-radio>
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value=""
            button-variant="outline-primary"
            style="margin-top: 0">
            全部
          </b-form-radio>
          <b-form-radio
            class="btn-outline-primary"
            name="isLike"
            value="1"
            button-variant="outline-primary">
            已收藏
          </b-form-radio>
        </b-form-radio-group>
      </b-col>
    </b-row>
  </div>
</template>

<!--suppress JSUnusedGlobalSymbols -->
<script>
// noinspection ES6CheckImport
import { BInputGroup, BFormInput, BInputGroupAppend, BButton, BFormRadio, BFormRadioGroup } from 'bootstrap-vue'
export default {
  name: 'IndexHeader',
  components: {
    'b-input-group': BInputGroup,
    'b-form-input': BFormInput,
    'b-input-group-append': BInputGroupAppend,
    'b-button': BButton,
    'b-form-radio': BFormRadio,
    'b-form-radio-group': BFormRadioGroup
  },
  data () {
    return {
      show: false,
      filter: {
        designation: '',
        starName: '',
        isLike: ''
      }
    }
  },
  watch: {
    filter: {
      handler (newValue) {
        this.$emit('filter-change', newValue)
      },
      deep: true
    }
  }
}
</script>

<style scoped>
@import "ListHeader.css";
</style>
