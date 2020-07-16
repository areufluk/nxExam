<template>
  <div>
      <dashheader :firstname="$route.params.name" status="Student"/>
      <h1>Hellllloo</h1>
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
