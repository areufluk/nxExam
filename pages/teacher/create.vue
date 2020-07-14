<template>
    <div>
        <form>
            <v-text-field v-model="teacher_name" name="teacher_name" label="teacher name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="created_by" name="created_by" label="subject name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="subject_name" name="subject_name" label="teacher name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="subject_id" name="subject_id" label="subject id"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="start_time" name="start_time" label="start time"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="end_time" name="end_time" label="stop time"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="easy" name="easy" label="easy"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="medium" name="medium" label="medium"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="hard" name="hard" label="hard"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="backward" name="backward" label="backward"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="scoring_method" name="scoring_method" label="scoring method"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="show_score" name="show_score" label="show score"  hide-details="auto" ></v-text-field>
            <v-btn style="margin-top:1em">
                <a href="/teacher">
                    Save
                </a>
            </v-btn>
        </form>
    </div>
</template>

<script>
export default {
    layout:'header',
    data() {
        return {
            teacher_name:'chanayut',
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
}
</script>       

<style>
</style>