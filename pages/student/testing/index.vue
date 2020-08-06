<template>
  <v-app>
      <dashheader :firstname="name" status="Student"/>
        <v-card v-for="data in datas" :key="data.id" class="d-flex pl-5 mb-2">
            <v-row justify="center"> 
                <v-col sm="8" class="pb-0">
                    <v-text-field label="Question" v-model="data.text" outlined required></v-text-field>
                    <v-text-field label="Level" v-model="data.level" outlined required></v-text-field>
                    <v-row v-for="choice in data.arrChoice" :key="choice.id" justify="center"> 
                        <v-checkbox></v-checkbox>
                        <v-text-field v-model="choice.text"></v-text-field>
                    </v-row>
                </v-col>
            </v-row>
        </v-card>
        <v-row justify="center" class="mt-5">
            <v-btn color="success" class="mx-3" width="200px" height="50px">Submit!</v-btn>
        </v-row>
  </v-app>
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
