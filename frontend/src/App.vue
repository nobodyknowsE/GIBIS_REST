<template>
  <v-app>
    <AppBar/>
    <v-main>
      <ContentPanel/>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
  import AppBar from './components/AppBar.vue'
  import ContentPanel from './components/ContentPanel.vue'
</script>
