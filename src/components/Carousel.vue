<template>
  <div class="section-container" v-for="section in sections" :key="section.title">
    <h2 class="section-title">{{ section.title }}</h2>

    <vueper-slides
      class="no-shadow custom-slider"
      :visible-slides="3"
      slide-multiple
      :gap="3"
      :slide-ratio="1 / 4"
      :dragging-distance="200"
      :breakpoints="{ 800: { visibleSlides: 2, slideMultiple: 2 } }"
    >
      <vueper-slide
        v-for="slide in section.slides"
        :key="slide.id"
        :image="slide.image"
      >
        <template v-slot:content>
          {{ slide.caption }}
        </template>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  components: {
    VueperSlides,
    VueperSlide
  },
  props: {
    sections: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

.section-title {
  text-align: center;  /* Vycentrování nadpisu */
  margin-left: 20px;   /* Odsazení zleva */
  margin-right: 20px;  /* Odsazení zprava */
}

.section-container {
  margin-bottom: 2rem;
}

.custom-slider .vueperslide__styled-shadow-left,
.custom-slider .vueperslide__styled-shadow-right {
  display: none;
}

.vueperslide__content {
  text-align: center;
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  color: grey;
}

.no-shadow {
  box-shadow: none;
}

.vueperslides {
  --arrows-size: 20px;
  --arrows-bg-color: transparent;
}

.vueperslides--arrows .vueperslides__arrow {
  color: grey;
}

.vueperslides--bullets .vueperslides__bullets {
  bottom: 10px;
  z-index: 1;
}

.vueperslides--bullets .vueperslides__bullet {
  width: 8px;
  height: 8px;
  margin: 0 4px;
  background-color: grey;
  opacity: 0.5;
}

.vueperslides--bullets .vueperslides__bullet.is-active {
  opacity: 1;
}

@media (max-width: 640px) {
  .vueperslide__content {
    bottom: 10px;
  }
}
</style>
