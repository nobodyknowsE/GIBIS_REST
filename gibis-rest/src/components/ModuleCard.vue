<template>
    <v-card 
        color="teal-lighten-2" 
        class="ma-3" 
        elevation="4" 
        variant="tonal"
        >
        <v-card-item>
            <div class="text-overline">{{ moduleName }}</div>
            <div v-for="dozent in dozenten">{{ dozent }}</div>
            <div>{{ ects }} ECTS</div>
        </v-card-item>
    </v-card>
</template>
  
<script lang="ts" setup>
    import { defineProps } from 'vue'

    const props = defineProps({
        moduleName: String,
        dozenten: [],
        ects: Number
    })

</script>