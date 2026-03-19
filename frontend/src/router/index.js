import { createRouter, createWebHistory } from 'vue-router'
import LoginTelaPrincipal from '../views/LoginTelaPrincipal.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginTelaPrincipal
  }
  // suas outras rotas...
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router