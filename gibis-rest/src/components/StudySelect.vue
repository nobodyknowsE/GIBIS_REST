<template>
    <v-sheet min-width="300">
        <v-select 
            v-model="selectedCourse"
            label="Wähle einen Studiengang aus"
            :items="items"
            @update:model-value="select"
        />
        <v-expansion-panels>
            <v-expansion-panel title="Modul hinzufügen" color="#009688">
                <v-expansion-panel-text>
                    <v-text-field placeholder="Name des Moduls" v-model="name"/>
                    <v-text-field placeholder="Name des Dozenten" v-model="dozent[0]"/>
                    <v-text-field placeholder="ECTS-Punkte" v-model="ects"/>
                    <v-btn text="hinzufügen" color="teal-lighten-5" @click="handlePost"/>
                </v-expansion-panel-text>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-sheet>
</template>
  
<script setup lang="ts">
    import { ref, onMounted, toRaw } from 'vue'
    import eventBus from '../eventBus'

    const items = ref([])
    const selectedCourse = ref('20inb')
    const name = ref()
    const dozent = ref([])
    const ects = ref()

    onMounted(async () => {
        fetch('http://127.0.0.1:5000/modules')
        .then(response => {
            return response.json()
        })
        .then(data => {
            items.value = toRaw(data.Studiengänge)
        })

        select()
    })

    function select() {
        fetch(`http://127.0.0.1:5000/course?id=${selectedCourse.value}`)
        .then(response => {
            const data = response.json()
            eventBus.emit('send-data-event', data)
        })
    }

    async function postData(data: any): Promise<any> {
    try {
        const response = await fetch(`http://127.0.0.1:5000/modules?id=${selectedCourse.value}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        });
        console.log("Status", response.status)
        return await response.json(); 
    } catch (error) {
        console.error('Fehler beim Ausführen des POST-Requests:', error);
        throw error;
    }
    }

    async function handlePost() {
    try {
            const data = {
            "Modul": name.value,
            "ECTS-Leistungspunkte": ects.value,
            "Dozierende": dozent.value
            }
            await postData(data)
        } catch (error) {
            console.error('Fehler beim Handhaben des POST-Requests:', error);
        }
    select()
    }
</script>
  