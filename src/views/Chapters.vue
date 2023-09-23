<template>
  <div class="container">
    <div v-for="section in sections" :key="section.id" class="section-container">
      <h1 @click="toggleSectionVisibility(section.id)">{{ section.title }}</h1>
      
      <vueper-slides 
        v-if="visibleSectionId === section.id"
        class="no-shadow"
        :visible-slides="3"
        slide-multiple
        :gap="10"
        :dragging-distance="200"
        :breakpoints="{ 800: { visibleSlides: 2, slideMultiple: 2 } }"
      >
        <vueper-slide 
          v-for="slide in section.slides" 
          :key="slide.id"
          :image="slide.image"
        >
          <template v-slot:content>
            <div class="caption-container">
              {{ slide.caption }}
            </div>
          </template>
        </vueper-slide>
      </vueper-slides>
    </div>
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
  data() {
    return {
      visibleSectionId: null,
      sections: [
        {
          id: 1,
          title: 'Chapter I',
          slides: [
            { id: 1, image: "carousel/chapter1/0.00023_001.avif", caption: "Popisek 1" },
            { id: 2, image: "carousel/chapter1/0.00023_002.avif", caption: "Popisek 2" },
            { id: 3, image: "carousel/chapter1/0.00023_003.avif", caption: "Popisek 3" },
            { id: 4, image: "carousel/chapter1/0.00023_004.avif", caption: "Popisek 1" },
            { id: 5, image: "carousel/chapter1/0.00023_005.avif", caption: "Popisek 2" },
            { id: 6, image: "carousel/chapter1/0.00023_006.avif", caption: "Popisek 3" },
          ]
        },
        {
          id: 2,
          title: 'Chapter II',
          slides: [
            { id: 1, image: "carousel/chapter2/0.00023_001.jpg", caption: "Popisek 1" }, // Upravil jsem "chapter1" na "chapter2"
            { id: 2, image: "carousel/chapter2/0.00023_002.jpg", caption: "Popisek 2" },
            { id: 3, image: "carousel/chapter2/0.00023_003.jpg", caption: "Popisek 3" },
            { id: 4, image: "carousel/chapter2/0.00023_004.jpg", caption: "Popisek 1" },
            { id: 5, image: "carousel/chapter2/0.00023_005.jpg", caption: "Popisek 2" },
            { id: 6, image: "carousel/chapter2/0.00023_006.jpg", caption: "Popisek 3" },
          ]
        },
        {
          id: 3,
          title: 'Chapter III',
          slides: [
            { id: 1, image: "carousel/chapter2/0.00023_001.jpg", caption: "Popisek 1" }, // Upravil jsem "chapter1" na "chapter2"
            { id: 2, image: "carousel/chapter2/0.00023_002.jpg", caption: "Popisek 2" },
            { id: 3, image: "carousel/chapter2/0.00023_003.jpg", caption: "Popisek 3" },
            { id: 4, image: "carousel/chapter2/0.00023_004.jpg", caption: "Popisek 1" },
            { id: 5, image: "carousel/chapter2/0.00023_005.jpg", caption: "Popisek 2" },
            { id: 6, image: "carousel/chapter2/0.00023_006.jpg", caption: "Popisek 3" },
          ]
        },
        {
          id: 4,
          title: 'Chapter IV',
          slides: [
            { id: 1, image: "carousel/chapter2/0.00023_001.jpg", caption: "Popisek 1" }, // Upravil jsem "chapter1" na "chapter2"
            { id: 2, image: "carousel/chapter2/0.00023_002.jpg", caption: "Popisek 2" },
            { id: 3, image: "carousel/chapter2/0.00023_003.jpg", caption: "Popisek 3" },
            { id: 4, image: "carousel/chapter2/0.00023_004.jpg", caption: "Popisek 1" },
            { id: 5, image: "carousel/chapter2/0.00023_005.jpg", caption: "Popisek 2" },
            { id: 6, image: "carousel/chapter2/0.00023_006.jpg", caption: "Popisek 3" },
          ]
        },
        {
          id: 5,
          title: 'Chapter V',
          slides: [
            { id: 1, image: "carousel/chapter2/0.00023_001.jpg", caption: "Popisek 1" }, // Upravil jsem "chapter1" na "chapter2"
            { id: 2, image: "carousel/chapter2/0.00023_002.jpg", caption: "Popisek 2" },
            { id: 3, image: "carousel/chapter2/0.00023_003.jpg", caption: "Popisek 3" },
            { id: 4, image: "carousel/chapter2/0.00023_004.jpg", caption: "Popisek 1" },
            { id: 5, image: "carousel/chapter2/0.00023_005.jpg", caption: "Popisek 2" },
            { id: 6, image: "carousel/chapter2/0.00023_006.jpg", caption: "Popisek 3" },
          ]
        },
      ]

    }
  },
  methods: {
    toggleSectionVisibility(sectionId) {
      if (this.visibleSectionId === sectionId) {
        this.visibleSectionId = null;
      } else {
        this.visibleSectionId = sectionId;
      }
    }
  }
}
</script>

<style scoped>
.container {
  padding-top: 70px;
  text-align: center;
  background-image: url('../assets/seamless_background.jpeg');
    background-repeat: repeat;
    background-size: auto;
    background-position: center center;
    min-height: calc(100vh - 70px);
  
}

.section-container {
  margin: 0 150px 0 150px;
  text-align: center;
  
}

h1 {
  font-family: "gunplay damage";
  color: rgba(157, 27, 30, 255);
  text-align: center;
  margin-bottom: 20px;
  font-size: 50px;
  padding-top: 20px;
  padding-bottom: 20px;
}

.vueper-slides {
  position: relative;
}




:deep(.vueperslides__inner) {
  padding-left: 50px;
  padding-right: 50px;
}


.vueper-slide {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: auto;
}

.vueper-slide img {
  width: 100%;
  height: auto;
  object-fit: contain;
  margin-bottom: 10px;
}

.caption-container {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 5px 0;
}

.vueper-slides .ps__arrow-prev, .vueper-slides .ps__arrow-next {
  top: 50%;
  transform: translateY(-50%);
  margin: 0 3%;
}





</style>
