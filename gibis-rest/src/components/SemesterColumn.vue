<template>
    <v-col>
        <v-card 
            title="n. Semester"
            class="text-teal-lighten-2"
            color="grey-lighten-5" 
            min-width="250" 
            min-height="700"
            >
            <v-card-item>
                <ModuleCard/>
                <ModuleCard/>
                <ModuleCard/>
                <ModuleCard/>
            </v-card-item>
        </v-card>
    </v-col>
  </template>
  
  <script setup lang="ts">
    import ModuleCard from './ModuleCard.vue'
  </script>
  