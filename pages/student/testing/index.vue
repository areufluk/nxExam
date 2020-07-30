<template>
  <div>
    <div @click="getURL()"> start </div>
    <!-- <div @click="log()"> confirm start </div> -->
    <div v-for="(problem, index) in data.data" :key="index">
        <p> 
            {{problem.problem}}
        </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    layout:'header',
    data() {
        return {
            subject_id:'',
            url:'',
            data:[{}]
        }
    },
    methods: {
        async getURL(){
            this.subject_id = localStorage.getItem('subject_id')
            this.url = 'http://127.0.0.1:8000/ShowSubjectFilter?id_exam='.concat(this.subject_id)
            this.data = await axios.get(this.url)
            console.log(this.data.data)
        },
        log(){
            console.log(this.data.data)
        }
    }
    // async asyncData(){
    //     const { data } = await axios.get(
            
    //     )
    //     console.log(data)
    //     return { datas : data }
    // },
}
</script>

<style>
.card {
    background-color: white;
    margin-bottom: 1rem;
    box-shadow: 0 0.1rem 0.5rem 0 rgba(202, 184, 184, 0.2);
    height: 20rem;
    border-radius: 1.2rem;
    background:linear-gradient( #CFCFCF 18%, #F1F1F1 18%);
}
.card-create {
    background-color: white;
    margin-bottom: 1rem;
    box-shadow: 0 0.1rem 0.5rem 0 rgba(0,0,0,0.2);
    height: 20rem;
    border-radius: 1.2rem;
    background: #F1F1F1;
}
.card-body {
    padding: 0 0.5rem 0.4rem 0;
}
@media (min-width: 600px){
    .col-sm-6 {
        float: left;
        width: 50%;
        position: relative;
        min-height: 1px;
        padding-right: 1rem;
        padding-left: 1rem;
    }
    .card-area{
    padding: 0 5rem 0 5rem;
    font-family: "Comic Sans MS", cursive, sans-serif;
    }
}
.col-lg-3{
    position: relative;
    min-height: 1px;
    padding-right: 2rem;
    padding-left: 2rem;
}
.card-area{
    padding: 0 1rem 0 1rem;
    font-family: "Comic Sans MS", cursive, sans-serif;
}
@media (min-width: 1800px){
    .col-lg-3 {
        float: left;
        width: 25%;
    }
    .card-area{
    padding: 0 15rem 0 15rem;
    font-family: "Comic Sans MS", cursive, sans-serif;
}
}
.title_subject{
    font-size: 1.2rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    text-align: center;
    font-weight: bold;
    margin-bottom: 1rem;
    padding-top: 0.8rem;
}
.detail{
    padding-top: 1rem;
    font-size: 0.9rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    padding-left: 1rem;
    font-weight: bold;
}
.list_menu{
    padding-left: 1rem;
    padding-top: 4rem;
    display: flex;
    flex-wrap: wrap;
}
.report{
    width: 45%;
    text-align: center;
    border-radius: 1.2rem;
    background-color: #FF8800;
    /* padding-top: 1rem; */
    font-size: 1.5rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    color: white;
    padding:0.1rem;
    cursor: pointer;
}
.edit{
    height: 2.5rem;
    padding:0 0 0 3.5rem
}
.delete{
    height: 2.5rem;
    padding:0 0 0 1rem
}
.title {
    font-size: 2rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    text-align: center;
    font-weight: bold;
    color: #BFBFBF;
}
.syntax {
    font-size: 10rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    text-align: center;
    color: #BFBFBF;
}
</style>