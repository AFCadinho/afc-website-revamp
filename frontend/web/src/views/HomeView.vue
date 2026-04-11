<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { fetchHomeMessage } from '../services/api';

const message = ref("Loading...")
const error = ref("")

onMounted( async () => {
    try {
        message.value = await fetchHomeMessage()
    } catch(err) {
        error.value = err instanceof Error ? err.message : "Something went wrong"
    }
})

</script>

<template>
    <h1>Home</h1>

    <p v-if="error">{{ error }}</p>
    <pre v-else>{{ message }}</pre>
</template>