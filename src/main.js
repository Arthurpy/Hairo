import { createApp } from 'vue';
import App from './App.vue';
import router from './routers/routers.js';
import axios from 'axios';
import GAuth from 'vue3-google-oauth2'
import './style.css';

// Create a new app instance
const app = createApp(App);

const gauthOption = {
    clientId: '281350104013-egts6r5aqhpim3je7c3kdf6t1a04trah.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'select_account'
}
app.use(GAuth, gauthOption)

// Set up axios for global use
app.config.globalProperties.$http = axios;

// Use the router with the app
app.use(router);

// Mount the app to the DOM
app.mount('#app');