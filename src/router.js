import { createRouter, createWebHistory } from 'vue-router'
import Chapters from './views/Chapters.vue'
import About from './views/About.vue'
import EShop from './views/EShop.vue'

const routes = [
  { path: '/chapters', component: Chapters },
  { path: '/about', component: About },
  { path: '/e-shop', component: EShop },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
