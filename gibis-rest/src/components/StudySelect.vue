<template>
    <v-sheet min-width="300">
        <v-select 
            v-model="selectedItem"
            label="Wähle einen Studiengang aus"
            :items="items"
        />
    </v-sheet>
</template>
  
<script setup lang="ts">
    import { ref } from 'vue'

    const selectedItem = ref(null)
    const items = ref([
    'item 1',
    'item 2',
    'item 3'
    ])
</script>
  