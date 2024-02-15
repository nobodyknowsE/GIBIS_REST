<template>
  <Login/>
  <v-sheet
    class="d-flex align-center justify-center flex-wrap text-center mx-auto px-4"
    rounded
  > 
    <SelectAndAdd/>
    <v-container class="pt-10">
      <v-row align="center" justify="center">
        <ModulesContainer/>
      </v-row>
    </v-container>
  </v-sheet>
</template>
  
<script setup lang="ts">
  import Login from './LoginDialog.vue'
  import ModulesContainer from './ModulesContainer.vue'
  import SelectAndAdd from './SelectAndAddSheet.vue'
</script>
  