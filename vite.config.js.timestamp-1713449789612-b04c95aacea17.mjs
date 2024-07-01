
import vue from "file:///Users/bouillardpierre/Desktop/hairo/Hairo/node_modules/@vitejs/plugin-vue/dist/index.mjs";
import { defineConfig } from "file:///Users/bouillardpierre/Desktop/hairo/Hairo/node_modules/vite/dist/node/index.js";
var vite_config_default = defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag === "plastic-button"
        }
      }
    })
  ]
});
export {
  vite_config_default as default
};
