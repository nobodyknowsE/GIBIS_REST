<template>
  <v-app>
    <v-app-bar 
      title="Modulübersicht"
      color="teal-accent-4"
    >
      <template v-slot:image>
          <v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"/>
      </template>
    </v-app-bar>
    <v-main>
      <v-select 
        v-model="selectedItem"
        label="Wähle einen Studiengang aus"
        :items="items"
      />
      <TestComponent/>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
  import TestComponent from './components/TestComponent.vue'
  import { ref } from 'vue'

  const selectedItem = ref(null)
  const items = ref([
    'item 1',
    'item 2',
    'item 3'
  ])
</script>
