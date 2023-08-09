<template>
  <Navbar />
  <router-view @chapter-changed="updateStyles" />
  <Footer />
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    Navbar,
    Footer
  },
  methods: {
    updateStyles({ font, color }) {
      document.documentElement.style.setProperty('--font', font);
      document.documentElement.style.setProperty('--color', color);
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
</style>
