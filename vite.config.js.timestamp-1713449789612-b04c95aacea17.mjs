// vite.config.js
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
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvVXNlcnMvYm91aWxsYXJkcGllcnJlL0Rlc2t0b3AvaGFpcm8vSGFpcm9cIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIi9Vc2Vycy9ib3VpbGxhcmRwaWVycmUvRGVza3RvcC9oYWlyby9IYWlyby92aXRlLmNvbmZpZy5qc1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vVXNlcnMvYm91aWxsYXJkcGllcnJlL0Rlc2t0b3AvaGFpcm8vSGFpcm8vdml0ZS5jb25maWcuanNcIjtpbXBvcnQgdnVlIGZyb20gXCJAdml0ZWpzL3BsdWdpbi12dWVcIjtcbmltcG9ydCB7IGRlZmluZUNvbmZpZyB9IGZyb20gXCJ2aXRlXCI7XG5cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIHBsdWdpbnM6IFtcbiAgICB2dWUoe1xuICAgICAgdGVtcGxhdGU6IHtcbiAgICAgICAgY29tcGlsZXJPcHRpb25zOiB7XG4gICAgICAgICAgaXNDdXN0b21FbGVtZW50OiB0YWcgPT4gdGFnID09PSAncGxhc3RpYy1idXR0b24nXG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KSxcbiAgXSxcbn0pO1xuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUFnVCxPQUFPLFNBQVM7QUFDaFUsU0FBUyxvQkFBb0I7QUFFN0IsSUFBTyxzQkFBUSxhQUFhO0FBQUEsRUFDMUIsU0FBUztBQUFBLElBQ1AsSUFBSTtBQUFBLE1BQ0YsVUFBVTtBQUFBLFFBQ1IsaUJBQWlCO0FBQUEsVUFDZixpQkFBaUIsU0FBTyxRQUFRO0FBQUEsUUFDbEM7QUFBQSxNQUNGO0FBQUEsSUFDRixDQUFDO0FBQUEsRUFDSDtBQUNGLENBQUM7IiwKICAibmFtZXMiOiBbXQp9Cg==
