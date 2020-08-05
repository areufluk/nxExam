<template>
    <v-app>
      <dashheader :firstname="name" status="Teacher"/>
      <v-row>
        <v-col>
          <h2 class="text-center my-4">Create Examination</h2>
          <v-row justify="center"> 
            <v-col sm="5" class="pb-0">
              <v-text-field label="Subject name" v-model="datas.subject_name" outlined required></v-text-field>
              <v-text-field label="Teacher name" v-model="datas.teacher_name" outlined required></v-text-field>
              <v-text-field label="Subject ID" v-model="datas.subject_id" outlined required></v-text-field>  
            </v-col>
            <v-col sm="5" class="pb-0">
              <v-text-field label="medium" v-model="datas.medium" outlined required></v-text-field>
              <v-text-field label="easy" v-model="datas.easy" outlined required></v-text-field>
              <v-text-field label="hard" v-model="datas.hard" outlined required></v-text-field>  
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-col sm="4" class="py-0">
              <v-menu
                  v-model="date_pick"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="datas.date"
                      label="Examination day"
                      prepend-inner-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="datas.date" @input="date_pick = false"></v-date-picker>
                </v-menu>
              </v-col>
              <v-col sm="3" class="py-0">
                <v-menu
                  ref="menu"
                  v-model="time_pick_1"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="datas.start_time"
                      label="Start time"
                      v-bind="attrs"
                      v-on="on"
                      outlined
                      readonly
                      prepend-inner-icon="mdi-clock-time-four-outline"
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="time_pick_1"
                    v-model="datas.start_time"
                    full-width
                    @click:minute="$refs.menu.save(datas.start_time)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
              <v-col sm="3" class="py-0">
                <v-menu
                  ref="menuu"
                  v-model="time_pick_2"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="datas.end_time"
                      label="End time"
                      v-bind="attrs"
                      v-on="on"
                      outlined
                      readonly
                      prepend-inner-icon="mdi-clock-time-four-outline"
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="time_pick_2"
                    full-width
                    v-model="datas.end_time"
                    @click:minute="$refs.menuu.save(datas.end_time)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
          </v-row>
          <v-row justify="center">
            <v-checkbox
              label="Backward?"
              v-model="datas.backward"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
            <v-checkbox
              label="Decrease?"
              v-model="datas.scoring_method"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
            <v-checkbox
              label="Show score?"
              v-model="datas.show_score"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
          </v-row>
          <v-row justify="center" class="mt-5">
            <v-btn color="success" class="mx-3" width="200px" height="50px" @click="postSubmit()">Create!</v-btn>
          </v-row>
        </v-col>
        <v-col sm="6">
          <v-dialog v-model="dialog" persistent max-width="800">
            <template v-slot:activator="{ on, attrs }">
              <v-card
                v-bind="attrs"
                v-on="on"
                min-height="70px"
                class="d-flex align-center justify-center mr-5 my-3"
                color="grey lighten-1"
              >
                <div class="d-flex">
                  <v-icon x-large>mdi-plus</v-icon>
                  <v-card-text>Question</v-card-text>
                </div>  
              </v-card>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">Create question</span>
              </v-card-title>
              <v-card-text  class="pb-0">
                <v-container>
                    <v-row>
                      <v-col cols="12" sm="9" class="pb-0">
                        <v-text-field label="Question*" required v-model="question.text"></v-text-field> 
                      </v-col>
                      <v-col cols="12" sm="3" class="pb-0">
                        <v-select v-model="question.level" :items="level" label="choose level"></v-select>
                      </v-col>
                    </v-row>
                    <v-col cols="12" class="pt-0">
                      <div v-for="ch in question.arrChoice" :key="ch.index">
                        <v-card
                          class="d-flex pl-5 mb-2"
                        >
                          <v-checkbox v-model="ch.isTrue"></v-checkbox>
                          <v-text-field v-model="ch.text" class="px-2" placeholder="choice..."></v-text-field>
                          <v-col sm="1" class="mt-1">  
                            <v-btn icon @click="delChoice(ch.index)">
                              <v-icon>mdi-close</v-icon>
                            </v-btn>
                          </v-col>
                        </v-card>
                      </div> 
                      <v-btn block x-large @click="addChoice()">Add choice</v-btn>
                    </v-col>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
                <v-btn color="blue darken-1" text @click="addQuestion()">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <div v-for="qu in datas.arrQuestion" :key="qu.index">
            <problem :level="qu.level" :text="qu.text"/>
          </div>  
        </v-col>
      </v-row>
    </v-app>
</template>

<script>
import axios from 'axios'
import dashheader from '@/components/dashHD'
import problem from '@/components/problemCard'
import formex from '@/components/examForm';
export default {
    components: {
        dashheader,
        problem,
        formex
    },
    data: () => ({
            name: (process.browser)? localStorage.getItem("name") : '',
            date_pick: false,
            time_pick_1: false,
            time_pick_2: false,
            dialog: false,
            datas : {
              teacher_name:'',
              subject_name:'',
              subject_id:'0',
              date: new Date().toISOString().substr(0, 10),
              start_time: null,
              end_time: null,
              easy: 0,
              medium: 0,
              hard: 0,
              backward: false,
              scoring_method: false,
              show_score: false,
              arrQuestion:[]
            },
            question: {
              level: 'easy',
              text: '',
              arrChoice: []
            },
            choice: {
              text: '',
              isTrue: false
            },
            level: ['easy','medium','hard']
      }
    ),
    methods: {
        async postSubmit() {
          await this.$store.dispatch('postSubmit', this.name, this.datas)
        },
        addQuestion() {
          this.datas.arrQuestion.push(this.question)
          this.question = {
            level: 'easy',
            text: '',
            arrChoice: []
          }
          this.dialog = false
        },
        addChoice() {
          this.question.arrChoice.push(this.choice)
          this.choice = {
            text: '',
            isTrue: false
          }
        },
        delChoice(index){
          this.question.arrChoice.splice(index, 1)
        }
    }
}
</script>       
