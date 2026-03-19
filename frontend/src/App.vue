<template>
  <router-view />
  <LoginTelaPrincipal />
</template>

<script>
import LoginTelaPrincipal from "@/views/LoginTelaPrincipal.vue";

export default {
  name: "App",
  components: {
    LoginTelaPrincipal,
  },
};
</script>

<style>
@import "@/assets/css/login_estilos_globais.css";
</style>
