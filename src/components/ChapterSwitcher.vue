<template>
    <div class="chapter-switcher">
      <button @click="prevChapter" :disabled="currentChapterIndex === 0">
        <i class="fas fa-chevron-left"></i>
      </button>
      <div class="current-chapter">{{ chapters[currentChapterIndex].title }}</div>
      <button @click="nextChapter" :disabled="currentChapterIndex === chapters.length - 1">
        <i class="fas fa-chevron-right"></i>
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChapterSwitcher',
    props: {
      chapters: {
        type: Array,
        required: true
      },
      currentChapterIndex: {
        type: Number,
        required: true
      }
    },
    methods: {
      prevChapter() {
        this.$emit('change-chapter', this.currentChapterIndex - 1);
      },
      nextChapter() {
        this.$emit('change-chapter', this.currentChapterIndex + 1);
      }
    }
  }
  </script>
  
  <style scoped>
  .chapter-switcher {
    display: flex;
    justify-content: flex-end; /* Align to the right */
    align-items: center;
    padding: 30px;
    margin-right: 75px;
    position: fixed;
    right: 0; /* Align to the right edge of the container */
    width: auto; /* Adjust the width as needed */
    top: 60px; /* Assuming your navbar height is 60px */
    background: transparent;
    z-index: 1000; /* Make sure it's above other content */
  }
  
  button {
    padding: 10px;
    background: none;
    border: none;
    cursor: pointer;
  }
  </style>
  