import { createWebHistory, createRouter } from "vue-router";
import login from './../vue/login.vue';
import dashboard from './../vue/dashboard.vue';
import Register from './../vue/register.vue';
import Landing from './../vue/landing.vue';


const routes = [
    {
      path: '/',
      name: 'home',
      component: Landing
    },
    {
      path: '/login',
      name: 'Login',
      component: login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: dashboard
    }

];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
export default router;