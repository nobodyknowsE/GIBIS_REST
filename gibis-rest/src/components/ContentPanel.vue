<template>
  <v-sheet
    class="d-flex align-center justify-center flex-wrap text-center mx-auto px-4"
    height="800"
    rounded
    min-width="1400"
  > 
    <StudySelect/>
    <v-container>
      <v-row align="center" justify="center">
        <SemesterColumn/>
        <SemesterColumn/>
        <SemesterColumn/>
        <SemesterColumn/>
      </v-row>
      <TestComponent/>
    </v-container>
  </v-sheet>
</template>
  
<script setup lang="ts">
  import TestComponent from './TestComponent.vue'
  import SemesterColumn from './SemesterColumn.vue'
  import StudySelect from './StudySelect.vue'
</script>
  