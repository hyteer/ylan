import Vue from 'vue'
import Router from 'vue-router'
import iView from 'iview'

Vue.use(Router)
Vue.use(iView)

import Hello from 'components/Hello'
import Home from 'components/Home'
import IviewUi from 'components/IviewUi'
import User from 'components/User'
// import Navbar from 'components/Navbar'

export default new Router({
  routes: [
    {path: '/', name: 'Hello', component: Hello},
    {path: '/iview', name: 'IviewUi', component: IviewUi},
    {path: '/home', name: 'Home', component: Home},
    {path: '/user/:id', name: 'User', component: User}
  ]
})
