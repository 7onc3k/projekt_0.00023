<template>
  <div>
    <ChapterSwitcher
      :chapters="chapters"
      :currentChapterIndex="currentChapterIndex"
      @change-chapter="changeChapter"
    />
    <Chapter
      :chapters="chapters"
      :currentChapterIndex="currentChapterIndex"
      :sections="chapter.sections"
      v-for="(chapter, index) in chapters"
      :key="index"
      v-show="index === currentChapterIndex"
    />
  </div>
</template>

<script>
import Chapter from "../components/Chapter.vue";
import ChapterSwitcher from "../components/ChapterSwitcher.vue";

import obrazek1 from "../assets/obrazek1.jpeg";
import obrazek2 from "../assets/obrazek2.jpeg";

export default {
  name: "Chapters",
  components: {
    Chapter,
    ChapterSwitcher,
  },
  data() {
    const chapters = [
      {
        title: "Chapter 1",
        font: "Montserrat",
        color: "#F26344",
        sections: [
          {
            image: obrazek1,
            title: "Section 1",
            text: "This is the text for section 1.",
          },

          {
            image: obrazek2,
            title: "Section 2",
            text: "This is the text for section 1.",
          },
          // More sections...
        ],
      },
      {
        title: "Chapter 2",
        font: "Times New Roman",
        color: "#555",
        sections: [
          {
            image: obrazek1,
            title: "Section 1",
            text: "This is the text for section 1.",
          },
          // More sections...
        ],
      },
      // More chapters...
    ];

    return {
      currentChapterIndex: chapters.length - 1, // Set to last chapter
      chapters,
    };
  },
  methods: {
    changeChapter(index) {
    this.currentChapterIndex = index;
    const font = this.chapters[this.currentChapterIndex].font;
    const color = this.chapters[this.currentChapterIndex].color;
    document.documentElement.style.setProperty('--font', font);
    document.documentElement.style.setProperty('--color', color);
    this.$emit('chapter-changed', { font, color });

    // Save the font and color in local storage
    localStorage.setItem('lastChapterFont', font);
    localStorage.setItem('lastChapterColor', color);
  },
  },

  mounted() {
    // This is a Vue lifecycle hook
    this.changeChapter(this.currentChapterIndex); // Call this method when the component is mounted
  },
};
</script>
