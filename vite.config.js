import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Vytvoříme konfigurační objekt pomocí defineConfig pro lepší type hinting a autodoplňování v editoru
export default defineConfig({
  plugins: [vue()],  // Přidáme plugin Vue.js

  build: {
    outDir: 'dist',  // Definuje výstupní složku
    base: '/projekt_0.00023/'  // Nastaví veřejnou cestu pro GitHub Pages
  }
})
