<template>
  <v-app>
      <dashheader :firstname="name" status="Student"/>
        <v-card v-for="data in selected_datas" :key="data.id" class="d-flex pl-5 mb-2">
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
      subject_index:'',
      selected_datas:[],
      easy:[],
      medium:[],
      hard:[],
      num_easy:'',
      num_medium:'',
      num_hard:'',
    }
  },
  methods: {
    async getQuestion() {
        try {
            // console.log(this.subject_index)
            this.datas = await this.$store.dispatch('getQuestion',this.subject_index)
            // console.log(this.datas)
        }
        catch(e){
            console.log(e)
        }
    },
    async compute(){
        for(let i = 0;i < this.datas.length; i++){
            console.log(this.datas[i].level)
            if(this.datas[i].level == 'easy')   this.easy.push(this.datas[i])
            else if(this.datas[i].level == 'medium')   this.medium.push(this.datas[i])
            else if(this.datas[i].level == 'hard')   this.hard.push(this.datas[i])
        }
        this.easy = this.easy.sort(() => Math.random() - 0.5)
        this.medium = this.medium.sort(() => Math.random() - 0.5)
        this.hard = this.hard.sort(() => Math.random() - 0.5)
        for(let i = 0; i<this.num_easy ;i++){
            this.selected_datas.push(this.easy[i])
        }
        for(let i = 0; i<this.num_medium ;i++){
            this.selected_datas.push(this.medium[i])
        }
        for(let i = 0; i<this.num_hard ;i++){
            this.selected_datas.push(this.hard[i])
        }
        console.log(this.selected_datas)
    }
  },
  async mounted() {
      this.subject_index = await localStorage.getItem("join_subjectIndex")
      this.num_easy = await localStorage.getItem("num_easy")
      this.num_medium = await localStorage.getItem("num_medium")
      this.num_hard = await localStorage.getItem("num_hard")
    //   console.log(this.num_easy)
    //   console.log(this.num_medium)
    //   console.log(this.num_hard)
      await this.getQuestion()
      await this.compute()
  }
}
</script>
