import { createWebHistory, createRouter } from "vue-router";
import login from './../vue/login.vue';
import dashboard from './../vue/dashboard.vue';
import Register from './../vue/register.vue';
import Landing from './../vue/landing.vue';
import ressources from './../vue/ressources.vue';
import revisions from './../vue/revision.vue';
import Agenda from "../vue/agenda.vue";
import Quiz from "../vue/quiz.vue";

import CourseDetails from './../vue/CourseDetails.vue';
import ReadCours from './../vue/ReadCours.vue';

const routes = [
    {
      path: '/',
      name: 'home',
      component: Landing,
    },
    {
      path: '/login',
      name: 'Login',
      component: login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: dashboard,
        meta: { requiresAuth: true }
    },
    {
      path: '/ressources',
      name: 'ressources',
      component: ressources,
      meta: { requiresAuth: true }
    },
    {
      path: '/revisions',
      name: 'revisions',
      component: revisions,
      meta: { requiresAuth: true }
    },
    {
      path: '/agenda',
      name: 'agenda',
      component: Agenda,
      meta: { requiresAuth: true }
    },
    {
      path: '/course/:courseName',
      name: 'CourseDetails',
      component: CourseDetails,
      props: true,
      meta: { requiresAuth: true }
    },
    {
      path: '/cours/:courseName/:fileName',
      name: 'ReadCours',
      component: ReadCours,
      props: true,
      meta: { requiresAuth: true }
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: Quiz,
      meta: { requiresAuth: true }
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/'
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!localStorage.getItem('authToken')) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            });
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
