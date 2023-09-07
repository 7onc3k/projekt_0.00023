<template>
  <div class="carousel-container">
    <vueper-slides class="carousel" :options="carouselOptions">
      <vueper-slide v-for="(item, index) in items" :key="index">
        <img :src="item.image" :alt="item.description">
        <p>{{ item.description }}</p>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides';
import 'vueperslides/dist/vueperslides.css';

export default {
  components: {
    VueperSlides,
    VueperSlide,
  },
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      carouselOptions: {
        arrows: true,
        draggable: true,
      },
    };
  },
};
</script>


<style scoped>
.carousel-container {
  /* Styles for carousel container */
}

.carousel {
  /* Styles for carousel */ 
}
</style>
