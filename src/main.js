import { createApp } from 'vue';
import App from './App.vue';
import router from './routers/routers.js';
import './style.css';

createApp(App).use(router).mount('#app');