<template>
  <div class="chapters">
    <button class="chapter-button" @click="toggleCarousel">Chapter I.</button>
    <button class="chapter-button" @click="toggleCarousel">Chapter II.</button>
    <button class="chapter-button" @click="toggleCarousel">Chapter III.</button>
    <Carousel v-if="showCarousel" :items="carouselItems" />
  </div>
</template>

<script>
import Carousel from '../components/Carousel.vue';

export default {
  components: {
    Carousel,
  },
  data() {
    return {
      showCarousel: false,
      carouselItems: [
        { image: 'image1.jpg', description: 'Popisek 1' },
        { image: 'image2.jpg', description: 'Popisek 2' },
        // ...
      ],
    };
  },
  methods: {
    toggleCarousel() {
      this.showCarousel = !this.showCarousel;
    },
  },
};
</script>


<style scoped>
.chapters {
  background: url("../assets/background.jpeg") no-repeat center center fixed;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.chapter-button {
  font-family: 'Gunplay Damage', sans-serif;
  font-size: 40px;
  color: #951812;
  text-decoration: none;
  margin: 50px;
  background: none;
  border: none;
  cursor: pointer;
}
</style>
