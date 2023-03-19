<template>
  <v-app>
    <v-main>
      <v-app-bar>
        <v-app-bar-title>Scrabble</v-app-bar-title>
        <v-spacer/>
        <a href="https://github.com/Franco-from-Owlish/scrabble" class="bar-link my-auto mx-10 pa-0">
            <v-icon size="x-large" color="black">
              mdi-github
            </v-icon>
        </a>
      </v-app-bar>
      <v-divider/>
      <v-container class="content-div">
        <Scrabble class="my-10 mx-auto"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import Scrabble from "@/components/Scrabble.vue";
</script>

<style scoped lang="scss">
  .content-div {
    width: 80%;
  }

  .bar-link {
    text-decoration: none;
    &:active {
      text-decoration: none;
    }
    &:hover {
      text-decoration: none;
    }
    &:visited {
      text-decoration: none;
    }
  }
</style>
