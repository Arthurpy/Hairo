import { createApp } from 'vue';
import App from './App.vue';
import router from './routers/routers.js';
import axios from 'axios';
import './style.css'

// Create a new app instance
const app = createApp(App);

// Set up axios for global use
app.config.globalProperties.$http = axios;

// Use the router with the app
app.use(router);

// Mount the app to the DOM
app.mount('#app');