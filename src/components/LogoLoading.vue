<template>
  <div
    class="number-display"
    :style="{ '--text-color': inOverlay ? 'rgba(218,218,218,255)' : 'rgba(157, 27, 30, 255)' }"
  >
    {{ animatedNumber }}
  </div>
</template>

<script>
export default {
  name: 'LogoLoading',
  props: {
    inOverlay: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    currentNumber: 0.00000,
    targetNumber: 0.00023,
    duration: 3000, // Doba trvání animace v milisekundách
    startTime: null
  }),
  computed: {
    animatedNumber() {
      return this.currentNumber.toFixed(5);
    }
  },
  methods: {
    animateNumber(timestamp) {
      if (!this.startTime) this.startTime = timestamp;
      const elapsed = timestamp - this.startTime;

      // Vypočítáme, jaký podíl z celkové doby trvání animace již uplynul
      const progress = Math.min(elapsed / this.duration, 1);
      
      // Nastavíme hodnotu currentNumber na základě průběhu
      this.currentNumber = progress * this.targetNumber;

      // Pokračujeme v animaci, dokud neprojde celá doba trvání
      if (progress < 1) {
        requestAnimationFrame(this.animateNumber);
      }
    }
  },
  mounted() {
    requestAnimationFrame(this.animateNumber);
  }
};
</script>

<style scoped>
.number-display {
  padding-top: 25px;
  font-size: 6em; /* Adjust size as necessary */
  font-weight: bold;
  margin-bottom: 2em;
  font-family: "Gunplay Damage", Courier, monospace; 
  color: var(--text-color);
}
</style>