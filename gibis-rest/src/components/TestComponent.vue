<template>
    <v-btn @click="fetchDataFromAPI">Get Modules</v-btn>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import axios from 'axios'

const apiData = ref([])

const fetchDataFromAPI = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/modules')
    apiData.value = response.data
    console.log(apiData.value)
  } catch (error) {
    console.error('Fehler beim Abrufen der Daten:', error)
  }
}
</script>