import { createWebHistory, createRouter } from "vue-router";
import login from './../vue/login.vue';
import dashboard from './../vue/dashboard.vue';
import Register from './../vue/register.vue';
import Landing from './../vue/landing.vue';
import caspratique from './../vue/caspratique.vue';


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
    },
    // {
    //   path: '/revision',
    //   name: 'revision',
    // }
    // {
    //   path: '/ressources',
    //   name: 'ressources',
    // }
    // {
    //   path: '/agenda',
    //   name: 'agenda',
    // }
    // {
    //   path: '/messagerie',
    //   name: 'messagerie',
    // }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
export default router;