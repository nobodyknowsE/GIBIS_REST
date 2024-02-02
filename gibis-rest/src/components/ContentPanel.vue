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
      </v-row>
    </v-container>
  </v-sheet>
</template>
  
<script setup lang="ts">
  import SemesterColumn from './SemesterColumn.vue'
  import StudySelect from './StudySelect.vue'
</script>
  