<template>
        <v-card 
            class="text-teal-lighten-2 pt-5"
            color="grey-lighten-5" 
            min-height="700"
            >
            <v-row>
                <v-card-item v-for="modul in receivedData">
                    <v-col>
                        <ModuleCard 
                        :moduleName="modul.Modul" 
                        :ects="modul['ECTS-Leistungspunkte']" 
                        :dozenten="modul['Dozierende']"
                        />
                    </v-col>
                </v-card-item>
             </v-row>
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
  