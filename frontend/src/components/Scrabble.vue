<template>
  <v-form v-model="valid" @submit.prevent="submit" class="pa-10 bg-grey-darken-4">
    <v-card-title>
      Take scrabble seriously...
    </v-card-title>
    <v-card-subtitle>
      Anything worth doing is worth overdoing.
    </v-card-subtitle>
    <v-card class="ma-auto mt-10 pa-8" color="grey-darken-3">
      <v-defaults-provider :defaults="ComponentDefaults">
        <v-text-field
          v-model="sentence"
          placeholder="Type a sentence"
          required
          clearable
        />
        <v-btn @click="submit">
          Submit
        </v-btn>
        <v-text-field
          v-model="newSentence"
          readonly
          class="mt-10 mx-auto"
        />
      </v-defaults-provider>
    </v-card>
  </v-form>
</template>

<script setup lang="ts">
import {ref} from "vue";

const valid = ref<boolean>(false);
const sentence = ref<string|null>(null);
const newSentence = ref<string|null>(null);

const ComponentDefaults = {
  VBtn: {
    color: "primary",
    block: true
  },
  VTextField: {
    color: "grey-lighten-1",
    variant: "outlined",
  }
}

async function submit() {
  if (!valid) return
  const form = new FormData();
  form.append("sentence", String(sentence.value));
  const requestOptions: RequestInit = {
    method: "POST",
    body: form,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow"
  };
  const response = await fetch('https://francogcc.pythonanywhere.com/api/sentence', requestOptions);
  console.log(response)
  const json = await response.json()
  console.log(json)
  if (response.status === 200) {
    const json = await response.json()
    console.log(json)
    newSentence.value = (await response.json())["new_sentence"];
  } else {
    newSentence.value = null;
  }
}

</script>

<style scoped lang="scss">

</style>
