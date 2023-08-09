<template>
  <div class="container">
    <LogoLoading class="logo" />
    <p class="description">
      0.00023 Was Created In 2022 By Mr. 23. The Main Vision Was To Combine The Beauty Of Destruction With Perfection Which Is Reflected In Everyday Life.
    </p>
  </div>
</template>

<script>
import LogoLoading from '../components/LogoLoading.vue';

export default {
  name: 'About',
  components: {
    LogoLoading
  }
};
</script>

<style scoped>
.container {
  position: relative;
  height: calc(100vh + 60px); /* Adjust 60px based on your Navbar's height */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: url("../assets/background.jpeg") no-repeat center center fixed;
  background-size: cover;
  text-align: center;
  color: var(--color);
  font-family: var(--font), sans-serif;
  z-index: -1;
  
}

.logo {
  height: auto;
  margin-bottom: 5px;

}

.description {
  font-size: 1.2em;
  padding-left: 500px;
  padding-right: 500px;
  margin-bottom: 100px;
}
</style>
