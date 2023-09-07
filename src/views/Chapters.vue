<template>
  <div class="chapters">
    <div :class="{ 'chapter-buttons': true, 'move-to-bottom': showCarousel }">
      <button class="chapter-button" @click="toggleCarousel(1)">Chapter I.</button>
      <button class="chapter-button" @click="toggleCarousel(2)">Chapter II.</button>
      <button class="chapter-button" @click="toggleCarousel(3)">Chapter III.</button>
    </div>
    <transition name="fade">
      <Carousel v-if="showCarousel" :items="carouselItems" />
    </transition>
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
      carouselItems: [],
    };
  },
  methods: {
    toggleCarousel(chapter) {
      this.showCarousel = !this.showCarousel;
      this.carouselItems = this.getCarouselItemsForChapter(chapter);
    },
    getCarouselItemsForChapter(chapter) {
      const importImage = (name) => {
        return new URL(`../assets/carousel/chapter${chapter}/${name}.jpg`, import.meta.url).href;
      };

      switch (chapter) {
        case 1:
          return [
            {
              image: importImage('0.00023_001'),
              description: 'Popisek 1',
            },
            {
              image: importImage('0.00023_002'),
              description: 'Popisek 2',
            },
            // ...
          ];
        case 2:
          return [
            // Add carousel items for chapter 2
          ];
        case 3:
          return [
            // Add carousel items for chapter 3
          ];
        default:
          return [];
      }
    },
  },
};
</script>


<style scoped>
/* Styles */
</style>

<style scoped>
.chapters {
  background: url("../assets/background.jpeg") no-repeat center center fixed;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}

.chapter-buttons {
  transition: all 0.5s ease;
}

.chapter-buttons.move-to-bottom {
  position: absolute;
  bottom: 0;
}

.chapter-button {
  font-family: "Gunplay Damage", sans-serif;
  font-size: 40px;
  color: #951812;
  text-decoration: none;
  margin: 50px;
  background: none;
  border: none;
  cursor: pointer;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
