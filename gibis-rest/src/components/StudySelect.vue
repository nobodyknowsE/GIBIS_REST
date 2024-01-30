<template>
    <v-sheet min-width="300">
        <v-select 
            label="Wähle einen Studiengang aus"
            :items="items"
        />
    </v-sheet>
</template>
  
<script setup lang="ts">
    import { ref, onMounted, toRaw } from 'vue'

    const items = ref([])

    onMounted(async () => {
        fetch('http://127.0.0.1:5000/modules')
        .then(response => {
            return response.json()
        })
        .then(data => {
            items.value = toRaw(data.Studiengänge)
        })
    })
</script>
  