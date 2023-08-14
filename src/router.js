import { createRouter, createWebHistory } from 'vue-router'
import Chapters from './views/Chapters.vue'
import About from './views/About.vue'
import EShop from './views/EShop.vue'
import Home from './views/Home.vue'  // Nový import

const routes = [
  { path: '/', redirect: '/home' },  // Přesměrování kořenové cesty na /home
  { path: '/home', component: Home },  // Nastavíme stránku Home pro cestu /home
  { path: '/chapters', component: Chapters },
  { path: '/about', component: About },
  { path: '/e-shop', component: EShop },
]


const router = createRouter({
  history: createWebHistory(),
  routes,
})


export default router
