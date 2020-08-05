import axios from 'axios'

export const state = () => ({
  user_session: null,
  name: null
})

export const mutations = {
  SET_SESSION (state, session) {
    state.user_session = session
  },
  SET_NAME (state, name) {
    state.name = name
  }
}

export const actions = {
  async login ({ commit }) {
    var obj = null
    try{
        var provider = new this.$firebase.auth.GoogleAuthProvider()
        const result = await this.$firebase.auth().signInWithPopup(provider)
        obj = result.additionalUserInfo.profile
        //request token from django
        const token = await axios.post('http://127.0.0.1:8000/reqToken' ,{ obj })
        console.log(token.data.user_token)
        //save token to sessionStorage
        if(process.browser){
            localStorage.setItem("name", obj.given_name)
            localStorage.setItem("picture", obj.picture)
            localStorage.setItem("token", token.data.user_token)
        }
        //routing
        if(token.data.type == 2){
            this.$router.push('student')
        }else if(token.data.type == 3){
            this.$router.push('teacher')
        }  
    } catch (err) {
        console.log(err)
    }
  },

  async changeData({commit}, name) {
    const { data } = await axios.get(
        'http://127.0.0.1:8000/getSublist',{
            params: {
                name: name
            }
        }
    )
    return data 
}
}