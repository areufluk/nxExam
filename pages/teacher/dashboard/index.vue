<template>
    <div class="card-area">
        <div v-for="data in datas" :key="data.id" class="col-sm-6 col-lg-3">
            <div class="card">
                <div clsss="card-body">
                    <p class="title_subject" v-if="data.subject_name.length < 15"> {{ data.subject_name }} </p>
                    <p class="title_subject" v-else> {{ data.subject_name.substring(0,15) + ".." }} </p>
                    <p class="detail"> {{ "Subject ID : " + data.subject_id }} </p>
                    <p class="detail"> {{ "Teachere : " + data.teacher_name }} </p>
                    <p class="detail" v-if="data.start_time.substring(0,10) == data.end_time.substring(0,10)"> {{ "Date : " + data.start_time.substring(0,10) }} </p>
                    <p class="detail"> {{ "Time : " + data.start_time.substring(11,19) + " - " + data.end_time.substring(11,19)}} </p>
                    <div class="list_menu">
                        <div class="report">Report</div>
                        <img class="edit" src="~/assets/image/edit.svg">
                        <img class="delete" src="~/assets/image/recycle.svg">
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-6 col-lg-3"> 
            <a class="link" href="create">
                <div class="card-create">
                    <div class="card-body">
                        <p class="syntax"> + </p>
                        <p class="title"> Create Subject </p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    layouts:'header',
    async asyncData(){
        const { data } = await axios.get(
            'http://127.0.0.1:8000/ShowSubject'
        )
        return { datas : data}
    }
}
</script>

<style>
.card {
    background-color: white;
    margin-bottom: 1rem;
    box-shadow: 0 0.1rem 0.5rem 0 rgba(0,0,0,0.2);
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
    width: 35%;
    text-align: center;
    border-radius: 1.2rem;
    background-color: #FF8800;
    /* padding-top: 1rem; */
    font-size: 1.5rem;
    /* font-family: "Comic Sans MS", cursive, sans-serif; */
    color: white;
    padding:0.1rem
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
a {
    text-decoration: none !important;
}
</style>