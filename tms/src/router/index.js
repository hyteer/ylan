import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// import Hello from 'components/Hello'
import Home from 'components/Home'
import Navbar from 'components/Navbar'

export default new Router({
  routes: [
    {path: '/', name: 'Home', component: Home},
    {path: '/nav', name: 'navbar', component: Navbar}
    // {path: '/other',name: 'Other',component: Other}
  ]
})
