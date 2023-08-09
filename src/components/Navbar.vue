<template>
  <nav :class="{ scrolled: hasScrolled }">
    <div class="logo">
      <img src="../assets/logo.png" alt="Logo" />
    </div>
    <div class="links">
      <router-link
        to="/chapters"
        class="link"
        @mouseover="handleHover($event, '/chapters')"
        @mouseleave="cancelNavigation"
      >
        CHAPTERS
        <svg class="circle" viewBox="0 0 100 100">
          <path
            class="circle-background"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
          <path
            class="circle-path"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
        </svg>
      </router-link>
      <router-link
        to="/about"
        class="link"
        @mouseover="handleHover($event, '/about')"
        @mouseleave="cancelNavigation"
      >
        ABOUT
        <svg class="circle" viewBox="0 0 100 100">
          <path
            class="circle-background"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
          <path
            class="circle-path"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
        </svg>
      </router-link>
      <router-link
        to="/e-shop"
        class="link"
        @mouseover="handleHover($event, '/e-shop')"
        @mouseleave="cancelNavigation"
      >
        E-SHOP
        <svg class="circle" viewBox="0 0 100 100">
          <path
            class="circle-background"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
          <path
            class="circle-path"
            d="M50 10 a 40 40 0 0 1 0 80 a 40 40 0 0 1 0 -80"
          />
        </svg>
      </router-link>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "Navbar",
  setup() {
    const hasScrolled = ref(false);
    const router = useRouter();
    let navigationTimeout = null;

    const handleScroll = () => {
      hasScrolled.value = window.scrollY > 0;
    };

    const handleHover = (event, path) => {
      navigationTimeout=setTimeout(() => {
        router.push(path);
      }, 2000); // 2 sekundy, což odpovídá délce animace
    };

    const cancelNavigation = () => {
      clearTimeout(navigationTimeout); // Clear the timeout if the mouse leaves
    };

    onMounted(() => {
      window.addEventListener("scroll", handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener("scroll", handleScroll);
    });

    return { hasScrolled, handleHover, cancelNavigation }; // Make sure to return cancelNavigation
  },
};
</script>

<style scoped>
@keyframes fill {
  0% {
    stroke-dashoffset: 251.2;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

.logo {
  width: auto;
  height: 70px;
  display: flex;
  justify-content: flex-end; /* Zarovná logo vpravo */
  align-items: center; /* Zarovná vertikálně */
  padding-left: 50px; /* Přidá nějaký odstup od okraje */
}

.logo img {
  max-height: 100%; /* Zajistí, že logo zůstane ve výšce divu */
  max-width: 100%; /* Omezí šířku logo tak, aby se vešlo do divu */
}

nav {
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 1em 2em;
  transition: background-color 0.3s ease;
  font-family: var(--font), sans-serif;
  box-sizing: border-box;
}
nav .logo {
  font-weight: bold;
}

nav .links {
  display: flex;
  align-items: center;
  padding-right: 2em;
}

nav .links .link {
  position: relative;
  text-decoration: none;
  padding: 0.5em;
  margin: 0 1em;
  transition: padding 0.3s ease;
  color: var(--color);
  font-weight: bold;
  font-size: 1.2rem;
}

nav .links .link:hover {
  padding-right: 1em; /* Menší hodnota pro menší posun textu odkazu */
}

nav .links .link .circle {
  position: absolute;
  top: 50%;
  right: -0.5em; /* Menší hodnota pro posunutí kruhu blíže k odkazu */
  width: 0.75em; /* Zmenšená hodnota pro zmenšení kruhu */
  height: 0.75em; /* Zmenšená hodnota pro zmenšení kruhu */
  transform: translate(-50%, -50%);
  opacity: 0;
}
nav .links .link .circle .circle-background {
  fill: none;
  stroke: gray; /* Šedá barva pro pozadí kruhu */
  stroke-width: 15; /* Tloušťka pozadí kruhu */
}
nav .links .link .circle .circle-path {
  fill: none;
  stroke: var(--color);
  stroke-width: 20;
  stroke-dasharray: 251.2;
  stroke-dashoffset: 251.2;
  transition: opacity 0.3s ease, stroke-dashoffset 2s linear;
}

nav .links .link:hover .circle {
  opacity: 1;
}

nav .links .link:hover .circle .circle-path {
  stroke-dashoffset: 0;
}

nav.scrolled {
  background-color: transparent;
}

@media (max-width: 600px) {
  nav .links {
    flex-direction: column;
    align-items: center;
  }
}
</style>
