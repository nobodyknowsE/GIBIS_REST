<template>
   
        <v-card 
            title="Module"
            class="text-teal-lighten-2"
            color="grey-lighten-5" 
            min-width="250" 
            min-height="700"
            >
            <v-card-item v-for="modul in receivedData">
                <ModuleCard/>
                {{ modul.Modul }}
            </v-card-item>
        </v-card>

  </template>
  
<script setup lang="ts">
    import ModuleCard from './ModuleCard.vue'
    import { ref, onMounted } from 'vue';
    import eventBus from '../eventBus';

    const receivedData = ref([{}])

    const onDataEvent = async (data: any) => {
        const res = await data
        receivedData.value = res
    }

    onMounted(() => {
        eventBus.on('send-data-event', onDataEvent)
    })
</script>
  