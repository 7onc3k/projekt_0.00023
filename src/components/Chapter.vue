<template>
    <div class="chapter">
      <Section
        :chapters="chapters"
        :currentChapterIndex="currentChapterIndex"
        v-for="(section, index) in sections"
        :key="index"
        :image="section.image"
        :title="section.title"
        :text="section.text"
        :index="index + 1"
      />
    </div>
  </template>

<script>
import Section from './Section.vue'

export default {
  components: {
    Section
  },
  props: ['sections', 'chapters', 'currentChapterIndex']
}
</script>

<style>
.chapter .section {
  position: relative; /* z-index only works on positioned elements */
  z-index: -1; /* Set a negative z-index to put it behind other elements */

}

.text-container {
  z-index: 1;
  /* další styly... */
}

</style>
