<template>
    <div>
        <v-btn class="open-button" @click="openForm()">Option</v-btn>
        <v-btn class="save-button" @click="postSubmit()"> Save </v-btn>
        <div class="form-popup" id="myForm">
            <form class="form-container">
                <v-text-field v-model="teacher_name" name="teacher_name" label="teacher name"  hide-details="auto" ></v-text-field>
                <v-text-field v-model="created_by" name="created_by" label="created_by name"  hide-details="auto" ></v-text-field>
                <v-text-field v-model="subject_name" name="subject_name" label="subject name"  hide-details="auto" ></v-text-field>
                <v-text-field v-model="subject_id" name="subject_id" label="subject id"  hide-details="auto" ></v-text-field>
                <v-text-field type="datetime-local" v-model="start_time" name="start_time" label="start time"  hide-details="auto" ></v-text-field>
                <v-text-field type="datetime-local" v-model="end_time" name="end_time" label="stop time"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="easy" name="easy" label="easy"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="medium" name="medium" label="medium"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="hard" name="hard" label="hard"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="backward" name="backward" label="backward"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="scoring_method" name="scoring_method" label="scoring method"  hide-details="auto" ></v-text-field>
                <v-text-field type="number" v-model="show_score" name="show_score" label="show score"  hide-details="auto" ></v-text-field>
                <v-btn class="btn cancel" @click="closeForm()">Close</v-btn>
            </form>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
export default {
    layout:'header',
    data() {
        return {
            teacher_name:'',
            created_by:'',
            subject_name:'',
            subject_id:'',
            start_time:'',
            end_time:'',
            easy:0,
            medium:0,
            hard:0,
            backward:0,
            scoring_method:0,
            show_score:0
        }
    },
    methods: {
        async postSubmit() {
            await axios.get('http://127.0.0.1:8000/add')
            .then((res) => console.log(res.data))
            .catch((err) => console.log(err))
        },
        openForm() {
            document.getElementById("myForm").style.display = "block";
        },
        closeForm() {
            document.getElementById("myForm").style.display = "none";
        },
        onload(){
            var e=document.getElementById("refreshed");
            if(e.value=="no")e.value="yes";
            else{e.value="no";location.reload();}
            console.log('reload')
        }
    }
}
</script>       

<style>
.open-button {
  background-color: #555;
  color: white;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  padding: 1rem 2rem 2rem 1rem;
  bottom: 2rem;
  right: 2rem;
  width: 8rem;
}
.save-button {
  background-color: #555;
  color: white;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  padding: 1rem 2rem 2rem 1rem;
  bottom: 2rem;
  right: 11rem;
  width: 8rem;
}
.form-popup {
  display: none;
  position: fixed;
  bottom: 0;
  right: 1rem;
  border: 0.2rem solid #f1f1f1;
  z-index: 999;
}
.form-container {
  min-width: 25rem;
  padding: 0.5rem;
  background-color: white;
}
.form-container .btn {
  background-color: #4CAF50;
  color: black;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  margin:10px 0 10px 0;
  opacity: 0.8;
}
</style>