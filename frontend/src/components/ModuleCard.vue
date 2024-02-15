<template>
    <v-card 
        color="teal-lighten-2" 
        elevation="4" 
        variant="tonal"

        width="250"
        min-height="220"
        >
        <v-card-item>
            <div class="text-overline">{{ moduleName }}</div>
            <div v-if="dozenten">{{ dozenten[0] }}</div>
            <div v-if=" dozenten && dozenten.length > 1">[...]</div>
            <div>{{ ects }} ECTS</div>
        </v-card-item>
    </v-card>
</template>
  
<script lang="ts" setup>
    const props = defineProps({
        moduleName: String,
        dozenten: [],
        ects: Number
    })

</script>