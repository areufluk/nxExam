<template>
  <div>
      <dashheader :firstname="$store.state.name" status="Student"/>
  </div>
</template>

<script>
import dashheader from '@/components/dashHD'
export default {
  components: {
    dashheader
  }
}
</script>