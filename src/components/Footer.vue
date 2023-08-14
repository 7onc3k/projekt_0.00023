<template>
  <footer>
    <div class="container">
      <div class="contact">
        <h2>Contact</h2>
        <p><i class="fas fa-envelope"></i> example@example.com</p>
        <p><i class="fas fa-phone"></i> 123-456-7890</p>
        <p><i class="fab fa-instagram"></i> example</p>
      </div>
      <div class="newsletter">
        <h2>Newsletter</h2>
        <p>Subscribe to our newsletter for the latest updates</p>
        <div class="input-container">
          <input type="email" placeholder=" Your email" />
          <button>Subscribe</button>
        </div>
      </div>
      <div class="links">
        <h2>Links</h2>
        <router-link to="/chapters">Chapters</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/e-shop">E-Shop</router-link>
      </div>
    </div>
    <div class="logo-column">
      <img src="../assets/logo.png" alt="Logo" class="logo" />
      <p class="logo-text">Website by Tony Nguyen</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
footer {
  max-width: 100vw;
  padding: 1em 30px;
  background-color: #f8f8f8;
  font-family: var(--font), sans-serif;
  color: var(--color);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container {
  width: 98%;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.contact,
.newsletter,
.links {
  flex: 1;
  text-align: center;
  padding: 0.5em;
}

.contact {
  text-align: left;
}

.links {
  text-align: right;
}

h2 {
  margin-bottom: 0.5em;
}

a {
  display: block;
  margin-bottom: 1em;
  color: var(--color);
  text-decoration: none;
}

.input-container {
  display: flex;
  flex-direction: column;  /* Aby byl input a tlačítko pod sebou */
  gap: 0.5em;
  align-items: center;    /* Pro vycentrování inputu a tlačítka */
}

input,
button {
  width: 360px;
  padding: 0.5em;
  border-radius: 25px;
  border: 1px solid #ccc;
  font-size: 1em;
  height: 35px;
  box-sizing: border-box;
}

button {
  background-color: var(--color);
  border: none;
  cursor: pointer;
  color: #f8f8f8;
}

.logo-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  height: 50px;
  margin-bottom: 0;
  margin-top: 20px;
}

.logo-text {
  margin-top: 0;
  font-size: 0.8em;
  margin-bottom: 0 ;
}

.fas, .fab {
  margin-right: 10px;
}
</style>