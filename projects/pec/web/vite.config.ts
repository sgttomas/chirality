import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 4811,
    proxy: {
      // changeOrigin:false preserves the browser Host so the server's RV-21
      // same-origin guard (Origin host === Host) passes through the dev proxy
      '/api': { target: 'http://localhost:4810', changeOrigin: false },
    },
  },
  build: {
    outDir: 'dist',
  },
})
