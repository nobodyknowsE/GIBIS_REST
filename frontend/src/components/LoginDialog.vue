<template>
    <div class="text-center">
        <v-dialog
        v-model="dialog"
        width="auto"
        persistent
        >
            <v-card width="400">
                <v-btn disabled block text="Login" color="#009688"/>
                <v-card-item>
                    <v-text-field label="username" v-model="username"/>
                    <v-text-field label="password" v-model="password" type="password"/>
                    <v-alert 
                        title="Login fehlgeschlagen" 
                        text="Nutzername oder Passwort falsch" 
                        variant="tonal" 
                        type="error" 
                        v-model="alert" 
                    />
                </v-card-item>
                <v-card-actions>
                    <v-btn 
                        text="Submit"
                        block 
                        @click="login"  
                        color="#009688"
                    />
                </v-card-actions>
            </v-card>
    </v-dialog>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue'

    const dialog = ref(true)
    const loginStatus = ref()
    const username = ref()
    const password = ref()
    const alert = ref(false)

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
</script>