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
      name: (process.browser)? localStorage.getItem("name") : '',
      datas:[],
      subject_index:''
    }
  },
  methods: {
    async getQuestion() {
        try {
            console.log(this.subject_index)
            this.datas = await this.$store.dispatch('getQuestion',this.subject_index)
            console.log(this.datas)
        }
        catch(e){
            console.log(e)
        }
    }
  },
  async mounted() {
      this.subject_index = await localStorage.getItem("join_subjectIndex")
      await this.getQuestion()
  }
}
</script>
