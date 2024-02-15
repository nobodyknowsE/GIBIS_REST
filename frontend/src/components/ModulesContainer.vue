<template>
    <v-card 
        class="text-teal-lighten-2 pt-5"
        color="grey-lighten-5" 
        >
        <v-card-item>
            <v-row class="px-5 mb-0">
                <v-col v-for="modul in receivedData" cols="3" lg="3" md="4" sm="6">
                    <ModuleCard 
                    :moduleName="modul.Modul" 
                    :ects="modul['ECTS-Leistungspunkte']" 
                    :dozenten="modul['Dozierende']"
                    />
                </v-col>
    
            </v-row>
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
  