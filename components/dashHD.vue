<template>
    <v-container fluid="" class="head">
        <div class="h-1" style="height: 6vh">
            <v-icon color="primary" class="icon">mdi-book-open-outline</v-icon>
            <h3>NEXTEXAM</h3>
            <v-spacer></v-spacer>
            <h3 style="margin-right: 6%">Logout</h3>
        </div>
        <div class="h-2" style="height: 27vh">
            <h1 style="margin: 6% 6% 0px">{{firstname}}</h1>
            <h3 style="margin-left:6%">{{status}}</h3>
        </div>
    </v-container>    
</template>

<script>
export default {
    props: ['firstname','status']
}
</script>

<style scoped>
.head {
    background-color: coral;
}
.icon {
    margin: 0px 10px 0px 6%;
}

.h-1 {
  justify-content: center;
  align-items: center;
  display: flex;
  width: 100%;
}
.h-2{
  display: flex;  
  flex-direction: column;
}
</style>