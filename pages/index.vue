<template>
  <div>
    <div class="head">
      <v-icon class="icon">mdi-book-open-outline</v-icon>
      <h3>NEXTEXAM</h3>
      <v-spacer></v-spacer>
      <h3 style="margin-right: 6%">Create by CEKMITL</h3>
    </div>
    <div class="content">
      <h1>Just do it</h1>
      <h4 style="margin: 2vh 0px 6vh">show your knowledge here or try your luck</h4>
      <v-btn rounded x-large @click="signInWithPopup">
        <v-img src="/g-icon.png" class="g-icon"/>
        Sign in with Google
      </v-btn>  
    </div> 
  </div>
</template>

<script>
export default {
  methods: {
    async signInWithPopup() {
      try {
        await this.$store.dispatch('login')
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style scoped>
.icon {
    margin: 0px 10px 0px 6%;
}
.head {
  justify-content: center;
  align-items: center;
  display: flex;
  width: 100%;
  height: 10vh;
}
.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 90vh;
  padding-bottom: 10vh;
}
.g-icon {
  max-width: 25px;
  margin-right: 10px;
}
</style>
