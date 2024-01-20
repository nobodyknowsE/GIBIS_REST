<template>
    <v-sheet min-width="300">
        <v-select 
            label="Wähle einen Studiengang aus"
        />
    </v-sheet>
</template>
  
<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    const items = ref([])

    onMounted(async () => {
        try {
                const response = await axios.get('http://127.0.0.1:5000/modules')
                items.value = response.data
                console.log('call', items.value)
            } catch (error) {
                console.error('Fehler beim Abrufen der Daten:', error)
            }
    })
</script>
  