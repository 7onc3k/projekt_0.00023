<template>
    <div class="carousel-container">
      <div class="carousel">
        <Section
          :image="obrazek2"
          title="Název sekce 1"
          text="Text sekce 1"
          :index="0"
          class="carousel-item"
        />
  
        <Section
          :image="obrazek1"
          title="Název sekce 2"
          text="Text sekce 2"
          :index="1"
          class="carousel-item"
        />

        <Section
          :image="obrazek1"
          title="Název sekce 1212"
          text="Text sekce 2"
          :index="1"
          class="carousel-item"
        />
  
        <!-- Přidejte další sekce zde -->
      </div>
    </div>
  </template>
  
  <script>
  import Section from "../components/Section.vue";
  
  // Import obrázků
  import obrazek1Src from "../assets/obrazek1.jpeg";
  import obrazek2Src from "../assets/obrazek2.jpeg";
  
  export default {
    name: "Home",
    components: {
      Section,
    },
    data() {
      return {
        obrazek1: obrazek1Src,
        obrazek2: obrazek2Src,
      };
    },
    mounted() {
      setInterval(() => {
        this.carouselMove();
      }, 10000);
    },
    methods: {
      carouselMove() {
        const carousel = this.$el.querySelector(".carousel");
        carousel.style.transform = "translateX(-100%)";
        setTimeout(() => {
          const firstItem = carousel.querySelector(".carousel-item");
          carousel.appendChild(firstItem);
          carousel.style.transition = "none";
          carousel.style.transform = "translateX(0)";
          setTimeout(() => {
            carousel.style.transition = "transform 1s";
          }, 50);
        }, 1000);
      },
    },
  };
  </script>
  
  <style scoped>

 
  .carousel-container {
    overflow: hidden;
    position: relative;
    width: 100vw;
    height: 100vh;
  }
  
  .carousel {
    display: flex;
    width: 100%;
    height: 100%;
    transition: transform 1s;
  }
  
  .carousel-item {
    flex-shrink: 0;
    width: 100vw;
    height: 100vh;
  }
  </style>