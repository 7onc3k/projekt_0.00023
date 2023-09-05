<template>
  <div v-if="visible" class="overlay" :style="{opacity: overlayOpacity}">
    <LogoLoading in-overlay />
  </div>
</template>

<script>
import LogoLoading from './LogoLoading.vue';

export default {
  components: {
    LogoLoading
  },
  data() {
    return {
      visible: true,
      overlayOpacity: 1
    };
  },
  methods: {
    hideOverlay() {
      this.overlayOpacity = 0;
      setTimeout(() => {
        this.visible = false;
        this.$emit('overlayHidden');
      }, 1000);  // Očekáváme, že animace trvá 1 sekundu (dle nastavení v CSS)
    }
  },
  mounted() {
    setTimeout(this.hideOverlay, 3200);
  }
};
</script>

<style scoped>
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-image: linear-gradient(to right, white, black);
    z-index: 1000;
    transition: opacity 1s;  
    padding-top: 150px;
}
</style>