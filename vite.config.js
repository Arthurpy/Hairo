// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { copy } from 'vite-plugin-copy';

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: tag => tag === 'plastic-button'
        }
      }
    }),
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
  },
  define: {
    '__VUE_OPTIONS_API__': true,
    '__VUE_PROD_DEVTOOLS__': false,
    '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': true
  }
});
