<template>
    <div>
        
          <h2 class="text-center my-4">{{hText}}</h2>
          <v-row justify="center"> 
            <v-col sm="5" class="pb-0">
              <v-text-field label="Subject name"
                :value="value.a"
                v-on:input="change"
                ref="aa"
                outlined
                ></v-text-field>
              <v-text-field label="Teacher name" :value="value.b"
                v-on:input="change"
                ref="bb"
                 outlined required></v-text-field>
              <v-text-field label="Subject ID" outlined required></v-text-field>  
            </v-col>
            <v-col sm="5" class="pb-0">
              <v-text-field label="medium" outlined required></v-text-field>
              <v-text-field label="easy" outlined required></v-text-field>
              <v-text-field label="hard" outlined required></v-text-field>  
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
                      label="Examination day"
                      prepend-inner-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker @input="date_pick = false"></v-date-picker>
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
                    full-width
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
                  ></v-time-picker>
                </v-menu>
              </v-col>
          </v-row>
          <v-row justify="center">
            <v-checkbox
              label="Backward?"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
            <v-checkbox
              label="Decrease?"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
            <v-checkbox
              label="Show score?"
              required
              class="mt-0 mx-5"
            ></v-checkbox>
          </v-row>
    </div>
</template>

<script>
export default {
    props: ['value','hText'],
    data: ()=> ({
        date_pick: false,
        time_pick_1: false,
        time_pick_2: false
    }),
    methods: {
        change: function(){
            this.$emit('changeTitle', {
                a: this.$refs.aa.value,
                b: this.$refs.bb.value
            })
        }
    },
}
</script>