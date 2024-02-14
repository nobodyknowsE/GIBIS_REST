<template>

<!--LOGIN DIALOG-->
    <div class="text-center">
        <v-dialog
        v-model="dialog"
        width="auto"
        persistent
        >
            <v-card width="400" color="teal-lighten-5">
                <v-btn disabled block text="Login" color="#009688"/>
                <v-card-item>
                    <v-text-field label="username" v-model="username"/>
                    <v-text-field label="password" v-model="password" type="password"/>
                    <v-alert variant="tonal" type="error" title="Login fehlgeschlagen" text="Nutzername oder Passwort falsch" v-model="alert" />
                </v-card-item>
                <v-card-actions>
                    <v-btn block @click="login" text="Submit" color="#009688"/>
                </v-card-actions>
            </v-card>
    </v-dialog>
    </div>
  
    <v-sheet min-width="300">
        <!--SELECT-->
        <v-select 
            v-model="selectedCourse"
            label="Wähle einen Studiengang aus"
            :items="items"
            @update:model-value="select"
        />
        <!--ADD MODUL PANEL-->
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
    const dialog = ref(true)
    const username = ref()
    const password = ref()
    const loginStatus = ref()
    const alert = ref(false)

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

    async function postLoginData(): Promise<any> {
    try {
        const response = await fetch(`http://127.0.0.1:5000/login?username=${username.value}&password=${password.value}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        });
        loginStatus.value = response.status
        console.log("Status", response.status)
        return await response.json(); 
    } catch (error) {
        console.error('Fehler beim Ausführen des POST-Requests:', error);
        throw error;
    }
    }




    async function login() {
        try {
            await postLoginData()
        } catch (error) {
            console.error('Fehler beim Ausführen des POST-Requests(Login):', error);
            throw error;
        }
        if(loginStatus.value == '200') {
            dialog.value = false
        } else {
            alert.value = true
            console.log('Login failed')
        }
    }
</script>
  