import firebase from 'firebase'

var firebaseConfig = {
    apiKey: "AIzaSyBX-GNsgJlhNdYZPXPCSp0oxXuTNTWc49M",
    authDomain: "nxexam.firebaseapp.com",
    databaseURL: "https://nxexam.firebaseio.com",
    projectId: "nxexam",
    storageBucket: "nxexam.appspot.com",
    messagingSenderId: "324791212286",
    appId: "1:324791212286:web:fc6b6e56880d1564792daf",
    measurementId: "G-KCR57KDFJQ"

  };
  let app = null
  // prevent initializing firebase more than once
  if (!firebase.apps.length) { 
    app = firebase.initializeApp(firebaseConfig)
  }
  // inject it so it can be accessed as this.$firebase inside the project
  export default (ctx, inject) => {
    inject('firebase', firebase)
  }