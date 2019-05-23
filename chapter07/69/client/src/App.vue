<template>
  <div id="app">
    <h1>Artist Search Service</h1>
    <div>
      <search-input attr="name" />
      <search-input attr="aliases_name" />
      <search-input attr="tag" />
      <button @click="postSearch">search</button>
    </div>
  <div>
    {{ artistNames }}
  </div>
  </div>
</template>

<script>
import SearchInput from './components/SearchInput.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    SearchInput
  },
  data () {
    return {
      result: {
        'data': []
      }
    }
  },
  computed: {
    artistNames () {
      if (this.result['data'].length == 0) {
        return
      }
      return this.result['data'].map((obj) => obj.name)
    }
  },
  methods: {
    async postSearch () {
      const name = document.getElementById("name").value
      const aliasesName = document.getElementById("aliases_name").value
      const tag = document.getElementById("tag").value
      let params = '?'
      if (name != '') {
        params = params + `name=${name}&`
      }
      if (aliasesName != '') {
        params = params + `aliases_name=${aliasesName}&`
      }
      if (tag != '') {
        params = params + `tag=${tag}&`
      }
      params = params.slice(0, -1)
      
      this.result = await axios.get('http://localhost:5000/search' + params)
      console.log(this.result)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
