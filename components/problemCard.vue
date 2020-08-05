<template>
    <v-card class="mr-5 my-3" min-height="70px">
        <div class="d-flex">
            <v-card v-if="level === 'easy'" color="success" min-height="70px" min-width="50px"></v-card>
            <v-card v-else-if="level === 'medium'" color="warning" min-height="70px" min-width="50px"></v-card>
            <v-card v-else-if="level === 'hard'" color="error" min-height="70px" min-width="50px"></v-card>
            <v-col align-self="center">
                <v-card-text class="text-center">{{text}}</v-card-text>
            </v-col>
        </div>
    </v-card>
</template>

<script>
export default {
    props: ['level','text']
}
</script>