<template>    
    <v-card min-height="70px" class="mr-5 my-3" color="grey lighten-1">
        <div class="d-flex">
            <v-card v-if="ob.level === 'easy'" color="success" min-height="70px" min-width="50px"></v-card>
            <v-card v-else-if="ob.level === 'medium'" color="warning" min-height="70px" min-width="50px"></v-card>
            <v-card v-else-if="ob.level === 'hard'" color="error" min-height="70px" min-width="50px"></v-card>
            <v-col align-self="center" >
                <v-card-text class="text-center">{{ob.text}}</v-card-text>
            </v-col>
            <v-col align-self="center" sm="1">
                <v-btn icon @click="delQuestion()">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-col>
        </div> 
    </v-card>        
</template>

<script>
export default {
    props: ['level','text','ob'],
    data: () => ({
        dialog: false,
        levels: ['easy','medium','hard'],
        question: {
              level: '',
              text: '',
              add_score: 0,
              sub_score: 0,
              arrChoice: []
            },
        choice: {
            text: '',
            isTrue: false
        }    
    }),
    methods: {
        delQuestion() {
            this.$emit('delQuestion')
        }
    }
}
</script>