<template>
  <footer>
    <div class="container">
      <div class="newsletter">
        <h2>Newsletter</h2>
        <p>Subscribe to our newsletter for the latest updates</p>
        <div class="input-container">
          <input type="email" placeholder=" Your email" />
          <button>Subscribe</button>
        </div>
      </div>
      <div class="contact">
        <h2>Contact</h2>
        <p><i class="fas fa-envelope"></i> example@example.com</p>
        <p><i class="fas fa-phone"></i> 123-456-7890</p>
        <p><i class="fab fa-instagram"></i> example</p>
      </div>
      <div class="links">
        <h2>Links</h2>
        <router-link to="/chapters">Chapters</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/e-shop">E-Shop</router-link>
      </div>
      <div class="logo-column">
        <div class="logo-container">
          <img src="../assets/logo.png" alt="Logo" class="logo" />
          <p class="logo-text">Website by Tony Nguyen</p>
        </div>
      </div>
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
  max-width: 1440px;
  width: 100%;
  padding: 2em 30px; /* Adjusted padding to only add 30px on left and right */
  background-color: #f8f8f8;
  font-family: var(--font), sans-serif;
  color:  var(--color);
  box-sizing: border-box; /* This ensures padding is included in the width */
}

.container {
  display: flex;
  justify-content: space-between;
  box-sizing: border-box; /* This ensures padding is included in the width */
}

.newsletter,
.links,
.contact,
.logo-column {
  padding: 0 1em;
  text-align: left;
}
.newsletter{
  padding-left: 40px;
}

h2 {
  margin-bottom: 1em;
}

a {
  display: block;
  margin-bottom: 0.5em;
  color: var(--color);
  text-decoration: none;
}

.input-container {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}

input,
button {
  box-sizing: border-box;
  width: 100%;
  padding: 0.5em;
  border-radius: 25px;
  border: 1px solid #ccc;
  margin: 0;
}

button {
  color: #fff;
  background-color:  var(--color);
  border: none;
  cursor: pointer;
}

.logo-column {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-right: 40px;
}

.logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
  margin-right: 50px;
}

.logo,
.logo-text {
  max-width: 100%;
}

.logo {
  height: 75px;
}

.contact {
  font-size: 0.9em; /* Reduced font size */
}

.contact p {
  padding-top: 2px;
}

.fas, .fab {
  margin-right: 10px;
}
</style>
