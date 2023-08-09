<template>
    <div class="section">
    
      <img :src="image" alt="" />
      <div class="text-container" :class="{ 'justify-end': index % 2 === 0, 'justify-start': index % 2 !== 0 }">
        <div class="text">
          <h2>{{ title }}</h2>
          <p>{{ text }}</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Section",
  props: ['image', 'title', 'text', 'chapters', 'currentChapterIndex', 'index'] // přidáno 'index'
};
</script>



<style scoped>
.index{
    z-index: 2;

}
.section {
  position: relative;
  height: 100vh;
  background-size: cover;
  background-position: center;
  font-family: var(--font), sans-serif;
  color: var(--color);
  
}

.section-content {
  position: absolute;
  top: 50%;
  right: 50px;
  transform: translateY(-50%);
  
}

.section-title {
  font-size: 2em;
  margin-bottom: 20px;
}

.section-text {
  font-size: 1.2em;
  
}
.section {
  display: flex;
  /* další styly... */
}

.text-container {
  display: flex;
  flex-direction: column;
  justify-content: center; /* Center the text vertically */
}
.justify-end {
  align-items: flex-start; /* Align the text to the right */

  margin-left: 60vw;
}

.justify-start {
  align-items: flex-end; /* Align the text to the left */
   /* Temporary, for testing */
  padding-left: 20vw;
}

img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  position: absolute;
}
</style>
