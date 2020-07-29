<template>
    <div>
        <v-btn class="open-button" @click="openForm()">Option</v-btn>
        <v-btn class="save-button" @click="postSubmit(),log(),postProblem()"> Save </v-btn>
        <v-btn class="next-button" @click="next()"> Next </v-btn>
        <div class="form-popup" id="myForm">
            <form action="/action_page.php" class="form-container">
                <v-text-field v-model="teacher_name" name="teacher_name" label="teacher name"  hide-details="auto" ></v-text-field>
                <v-text-field v-model="created_by" name="created_by" label="created_by"  hide-details="auto" ></v-text-field>
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
        <div class="form-question">
            <v-col class="d-flex" cols="12" sm="10">
                <p class="topic">Question {{arrQuestion.length}}</p>
                <v-text-field v-model="question" name="question" style="padding:0 0 1rem 0"></v-text-field>
                
            </v-col>
            <div class="choice" v-for="(data,index) in arrChoice" :key="index">
                 <p class="topic">Choice {{index}}</p>
                <v-text-field v-model="data.choice" style="margin:0 0 0.5rem 0"></v-text-field>
                <v-checkbox v-model="data.IsTrue" :label="`Choice ${index.toString()} Is True `"></v-checkbox>
                <v-btn @click="deleteFind(index)"> delete</v-btn>
            </div>
            <v-col class="d-flex" cols="12" sm="2">
                <v-btn @click="addFind()" style="margin:2rem 0 0 0">Add Choice</v-btn>
                <div class="level">
                    <p class="topic">Select Level</p>
                    <select v-model="level" label="select level" id="country" name="country">
                        <option value="Easy">Easy</option>
                        <option value="Medium">Medium</option>
                        <option value="Hard">Hard</option>
                    </select>
                </div>
            </v-col>
            <v-col class="d-flex" cols="12" sm="10">
                <p class="topic">score_plus</p>
                <v-text-field v-model="score_plus" name="score_plus" style="padding:0 0 1rem 0"></v-text-field>
                <p class="topic">score_sub</p>
                <v-text-field v-model="score_sub" name="score_sub" style="padding:0 0 1rem 0"></v-text-field>
            </v-col>
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
            show_score:0,
            arrQuestion:[],
            question:'',
            arrChoice:[],
            choice:'',
            level:'',
            score_plus:0,
            score_sub:0,
            checkbox: true,
            sumChoice:[]
        }
    },
    methods: {
        async postSubmit() {
            await axios.post('http://127.0.0.1:8000/InsertSubject' ,{
            teacher_name:this.teacher_name,
            created_by:this.created_by,
            subject_name:this.subject_name,
            subject_id:this.subject_id,
            start_time:this.start_time,
            end_time:this.end_time,
            easy:this.easy,
            medium:this.medium,
            hard:this.hard,
            backward:this.backward,
            scoring_method:this.scoring_method,
            show_score:this.show_score
            })
            .then((res) => console.log(res.data))
            .catch((err) => console.log(err))
        },
        async postProblem() {
            this.arrQuestion.push({
                'id_exam':this.subject_id,
                'question':this.question,
                'level':this.level,
                'score_plus':this.score_plus,
                'score_sub':this.score_sub
            });
            for (let i=0;i<this.arrQuestion.length;i++){
                await axios.post('http://127.0.0.1:8000/InsertProb' ,{
                id_exam:this.arrQuestion[i].id_exam,
                problem:this.arrQuestion[i].question,
                level:this.arrQuestion[i].level,
                score_plus:this.arrQuestion[i].score_plus,
                score_sub:this.arrQuestion[i].score_sub 
            })
            .then((res) => console.log(res.data))
            .catch((err) => console.log(err))
            }
        },
        openForm() {
            document.getElementById("myForm").style.display = "block";
        },
        closeForm() {
            document.getElementById("myForm").style.display = "none";
        },
        addFind() {
            this.arrChoice.push({'choice':'',
                                'IsTrue':'',
                                'id_problem':this.subject_id.concat(this.arrQuestion.length.toString())
            });
            for (let i = 0 ; i < this.arrChoice.length ; i++){
                if (this.arrChoice[i].IsTrue != true){
                    this.arrChoice[i].IsTrue = false
                }
            }
        },
        deleteFind(index) {
            this.arrChoice.splice(index, 1);
        },
        log(){
            this.sumChoice.push(this.arrChoice)
            console.log(this.arrQuestion)
            // console.log(this.sumChoice[0][0])
            console.log(this.sumChoice)
        },
        next(){
            this.arrQuestion.push({
                'id_exam':this.subject_id,
                'question':this.question,
                'level':this.level,
                'score_plus':this.score_plus,
                'score_sub':this.score_sub
            });

            this.sumChoice.push(this.arrChoice)
            this.arrChoice.push({'choice':'',
                                'IsTrue':'',
                                'id_problem':''
            });
            
            this.id_exam=''
            this.question=''
            this.level=''
            this.score_plus=0
            this.score_sub=0
            this.arrChoice=[]
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

.next-button {
    background-color: #555;
  color: white;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  padding: 1rem 2rem 2rem 1rem;
  bottom: 2rem;
  right: 20rem;
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

.form-question{
    padding:2rem 0rem 2rem 12rem;
    margin-right: 30rem;
}

.choice{
    padding:1rem 0 0 0;
}


.level select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  -webkit-appearance: menulist;
}
.topic{
  margin:1.5rem 0 0 0;
  font-family: "Comic Sans MS", cursive, sans-serif;
  color:black;
  font-size:1rem;
  text-align: left; 
}
</style>