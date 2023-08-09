<template>
    <div class="container">
      <h1 class="title">Coming Soon</h1>
      <p class="description">
        We are working hard to bring you our new e-shop. Sign up below to get updates!
      </p>
      <form @submit.prevent="submitForm" class="form">
        <input type="email" id="email" v-model="email" required placeholder=" Enter your email" />
        <button type="submit">Sign Up</button>
      </form>
    </div>
</template>
  
  
  <script>
  export default {
    data() {
      return {
        email: ""
      };
    },
    methods: {
      submitForm() {
        // Replace this with your actual submission logic
        alert(`Subscribed with email: ${this.email}`);
        this.email = "";
      }
    }
  };
</script>
  

<style scoped>
.container {
  position: relative;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: url("../assets/background.jpeg") no-repeat center center fixed; /* Path to your background image */
  background-size: cover;
  text-align: center;
  padding: 10em;
  padding-top: 220px;
  padding-bottom: 300px;
  z-index: -1;
  color: var(--color);
  font-family: var(--font), sans-serif;
}

.title {
  font-size: 2.5em;
  
}

.description {
  font-size: 1.2em;
  
  margin-bottom: 2em;
}

.form {
  display: flex;
  gap: 1em; /* Space between the input and button */
  
}

input[type="email"] {
  padding: 0.5em;
  font-size: 1em;
  border-radius: 25px;
  width: 450px;
  border: 2px solid var(--color);
  
}
input[type="email"]::placeholder {
  color: var(--color);
}


button {
  padding: 0.5em 1em;
  font-size: 1em;
  color: #fff;
  background-color: var(--color);
  border: none;
  border-radius: 25px;
  cursor: pointer;
}


button {
  width: 200px; /* Adjust as needed */
  /* Other styles... */
}


</style>
