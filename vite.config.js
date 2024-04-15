// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { copy } from 'vite-plugin-copy';

export default defineConfig({
  plugins: [
    vue(),
    copy({
      targets: [
        { src: 'src/assets/**/*', dest: 'back/Hairo_Back/static/dist/assets' }
      ],
      hook: 'writeBundle' // Optionnel: spécifiez quand la copie doit avoir lieu
    })
  ],
  build: {
    outDir: 'back/Hairo_Back/static/dist',
    emptyOutDir: true, // Assurez-vous que ce paramètre correspond à vos besoins
    // Vos autres configurations de build ici...
  }
});
