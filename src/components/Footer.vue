<template>
  <footer>
    <div class="container">
      <div class="contact">
        
        <h3>Follow us</h3>
        <p><a href="https://www.instagram.com/0.00023_project/" target="_blank" rel="noopener noreferrer"> INSTAGRAM</a></p>
        <p><a href="https://www.youtube.com/@023_project" target="_blank" rel="noopener noreferrer"> YOUTUBE</a></p>
        <p><a href="https://www.tiktok.com/@0_00023r?_t=8fu1PpULuNN&_r=1" target="_blank" rel="noopener noreferrer">TIKTOK</a></p>
      
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
        <h3>Discover</h3>
        <router-link to="/chapters">CHAPTERS</router-link>
        <router-link to="/contact">CONTACT</router-link>
        <router-link to="/about">ABOUT</router-link>
        <router-link to="/e-shop">E-SHOP</router-link>
        
      </div>
    </div>
    <div class="logo-column">
      <img src="../assets/logo_znak.png" alt="Logo" class="logo" />
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
  width: 75%; /* upravená šířka kontejneru */
  display: flex;
  justify-content: space-between; /* zajistí stejný prostor mezi sloupci */
  align-items: flex-start;
  margin: 0 auto; /* vycentruje kontejner na střed stránky */
}

.contact,
.newsletter,
.links {
  flex: 1;  /* zajistí, že všechny sloupce budou mít stejnou šířku */
  text-align: center;
  padding: 0.5em;
  margin: 0 15px; /* přidáváme okraje na stranách pro každý sloupec */
}


.contact {
  text-align: left;
  padding-top: 50px;
  
}




.links {
  text-align: right;
  padding-top: 50px;
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
  height: 70px;
  margin-bottom: 0;
  margin-top: 20px;
  margin-bottom: 15px;
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