<template>
    <div>
      <Section 
        :image="obrazek2"
        title="Název sekce 1"
        text="Text sekce 1"
        :index="0" />
      
      <Section 
        :image="obrazek1"
        title="Název sekce 2"
        text="Text sekce 2"
        :index="1" />
    </div>
</template>

<script>
import Section from '../components/Section.vue'; 

// Import obrázků
import obrazek1Src from "../assets/obrazek1.jpeg";
import obrazek2Src from "../assets/obrazek2.jpeg";

export default {
    name: "Home",
    components: {
        Section 
    },
    data() {
        return {
            obrazek1: obrazek1Src,
            obrazek2: obrazek2Src
        }
    }
};
</script>

<style scoped>

</style>
