import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../view/HomeView.vue'
import LoginView from '../view/LoginView.vue'

const routes = [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginView },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router