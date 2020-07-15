<template>
  <div>
      <div class="header">
        <div class="head_sec1">
          <div class="space_left"></div>
          <div class="logo_web">
            <div class="detail_logo">
              <img class="icon" src="~/assets/image/book_logo.png">
              <p class=title_name>NEXTEXAM</p>
            </div>
          </div>
          <div class="space_center"></div>
          <div class="logout">
            <p>Logout</p>
          </div>
          <div class="space_left"></div>
        </div>
        <div class="head_sec2">
          <p>Kanisorn</p>
          <p class="orange">Teacher</p>
        </div>
      </div>
    <nuxt />
  </div>
</template>

<script>

</script>

<style >
.icon {
  width:auto;
  height: 2.5rem;
  margin: 1rem 2rem 0rem 3.5rem;
}
/* .v-toolbar__content{
  align-items:stretch;
} */
.title_name{
  margin:.7rem 0 0 0;
  font-family: "Comic Sans MS", cursive, sans-serif;
  color:white;
  font-size:1.5rem;
}
.header{
  height: 20rem;
  background-image: url(../assets/image/book_opa.jpg)
}
.head_sec1{
  display: flex;
  flex-wrap: wrap;
  /* height: 5em; */
  margin: 0 0 5rem 0;
}
.head_sec2{
  margin: 0 0 5em 3.5em;
  font-size:3rem;
  font-weight: bold;
  font-family: "Comic Sans MS", cursive, sans-serif;
  color:white;
}
.orange{
  color:orange;
  font-size:1.5rem;
}
.space_left,.space_right{
  width: 5%;
}
.logo_web{
  width:20%;
}
.space_center{
  width:50%
}
.logout{
  margin:1.5rem 0 0 0;
  width:20%;
  font-family: "Comic Sans MS", cursive, sans-serif;
  color:white;
  font-size:1rem;
  text-align: right;
}
.detail_logo{
  display: flex;
  flex-wrap: wrap;
}
</style>
