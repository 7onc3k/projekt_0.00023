<template>
  <div id="app">
    <LoadingOverlay @overlayHidden="handleOverlayHidden" />
    <Navbar />
    <router-view @chapter-changed="updateStyles" />
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import LoadingOverlay from './components/LoadingOverlay.vue'  // Přidáno

export default {
  components: {
    Navbar,
    Footer,
    LoadingOverlay  // Přidáno
  },
  methods: {
    updateStyles({ font, color }) {
      document.documentElement.style.setProperty('--font', font);
      document.documentElement.style.setProperty('--color', color);
    },
    handleOverlayHidden() {  // Přidáno
      console.log("Overlay je skrytý");
      // Zde můžete vykonat další akce, pokud je to třeba
    }
  },
  created() {
    const font = localStorage.getItem('lastChapterFont');
    const color = localStorage.getItem('lastChapterColor');
    if (font && color) {
      this.updateStyles({ font, color });
    }
  },
}
</script>

<style>
.header,
.footer,
body {
  font-family: var(--font), sans-serif;
  color: var(--color);
}

@font-face {
  font-family: 'Gunplay Damage';
  src: url('./assets/gunplay_damage.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}


</style>
