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
        console.log(obj)
    } catch (err) {
        console.log(err)
    }
    await axios.post('http://127.0.0.1:8000/reqToken' ,{ obj }).then( function(res) {
        //commit('SET_SESSION', data)
        console.log(res)
        commit('SET_NAME', obj.given_name)
        if (res.data == 200){
            return this.$router.push('student')
        }else if(res.data == 300){
            return this.$router.push('teacher')
        }
        return null
    }.bind(this))
  },

  /*async logout ({ commit }) {
    commit('SET_USER', null)
  }*/
}
