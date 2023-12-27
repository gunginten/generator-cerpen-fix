import { createRouter, createWebHistory } from 'vue-router'
import Generator from '../components/Generator.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'generator',
      component: Generator,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router
