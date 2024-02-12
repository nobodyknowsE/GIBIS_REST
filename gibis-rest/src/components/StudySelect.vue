<template>
    <v-sheet min-width="300">
        <v-select 
            v-model="selectedCourse"
            label="Wähle einen Studiengang aus"
            :items="items"
            @update:model-value="select"
        />
    </v-sheet>
</template>
  
<script setup lang="ts">
    import { ref, onMounted, toRaw } from 'vue'
    import eventBus from '../eventBus'

    const items = ref([])
    const selectedCourse = ref(null)

    onMounted(async () => {
        fetch('http://127.0.0.1:5000/modules')
        .then(response => {
            return response.json()
        })
        .then(data => {
            items.value = toRaw(data.Studiengänge)
        })
    })

    function select() {
        console.log(selectedCourse.value)
        fetch(`http://127.0.0.1:5000/course?id=${selectedCourse.value}`)
        .then(response => {
            const data = response.json()
            eventBus.emit('send-data-event', data)
            return data
        }) 
        .then(data => {
            console.log(data)
        })
    }
</script>
  