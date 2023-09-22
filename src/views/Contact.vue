<template>
  <div class="customer-service">
    <div class="content">
      <h1>CUSTOMER SERVICE</h1>
      <p class="email">xxx@xxx.com</p>
      <h1 class="collaboration-header">COLLABORATION</h1>
      <p class="email">xxx@xxx.com</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CustomerService',
};
</script>

<style scoped>
.customer-service {
  background: url("../assets/background.jpeg") no-repeat center center fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
}

.content {
  text-align: center;
}

.collaboration-header {
  margin-top: 50px; /* Upravte tuto hodnotu podle potřeby. */
}

.email {
  font-size: 1.2em; /* Zvětšení velikosti fontu pro e-maily. */
}
</style>
