import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Hello from 'components/Hello'
import Home from 'components/Home'
import User from 'components/User'
import UserHome from 'components/User/UserHome'
import UserProfile from 'components/User/Profile'
import UserPosts from 'components/User/UserPosts'
import ElementUI from 'components/ElementUI'
import elGrid from 'components/ElementUI/Grid'
import elMenu from 'components/ElementUI/Menu'
import elForm from 'components/ElementUI/Form'
import elButton from 'components/ElementUI/Button'

// import Navbar from 'components/Navbar'

export default new Router({
  routes: [
    {path: '/', name: 'Hello', component: Hello},
    {path: '/home', name: 'Home', component: Home},
    {
      path: '/element',
      name: 'ElementUI',
      component: ElementUI,
      children: [
        {
          // UserProfile will be rendered inside User's <router-view>
          // when /user/:id/profile is matched
          path: 'grid',
          component: elGrid
        },
        {
          path: 'menu',
          component: elMenu
        },
        {
          path: 'button',
          component: elButton
        },
        {
          path: 'form',
          component: elForm
        }
      ]
    },
    {
      path: '/user/:id',
      name: 'User',
      component: User,
      children: [
        {
          path: '',
          component: UserHome
        },
        {
          // UserProfile will be rendered inside User's <router-view>
          // when /user/:id/profile is matched
          path: 'profile',
          component: UserProfile
        },
        {
          // UserPosts will be rendered inside User's <router-view>
          // when /user/:id/posts is matched
          path: 'posts',
          component: UserPosts
        }
      ]
    }
  ]
})
