<template>
  <div>
    {{ attr }}:
    <input type="text" :name="attr" :id="attr"/>
  </div>
</template>

<script>
export default {
  props: ['attr']
}
</script>

<style scoped>

</style>
