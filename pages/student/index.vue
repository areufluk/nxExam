<template>
  <div>
      <dashheader :firstname="name" status="Student"/>
  </div>
</template>

<script>
import dashheader from '@/components/dashHD'
export default {
  components: {
    dashheader
  },
  data(){
    return{
      name: (process.browser)? localStorage.getItem("name") : ''
    }
  }
}
</script>