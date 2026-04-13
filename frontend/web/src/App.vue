<script setup lang="ts">
</script>

<template>
  <header>
    <h1>Welcome</h1>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink :to="{ name: 'login' }">Login</RouterLink>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
  
</template>

<style>
body {
  margin: 0;
  font-family: system-ui, sans-serif;
}
</style>