<template>
    <v-btn @click="goLogin">
    Go Login
    </v-btn>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goLogin = () => {
	router.push({ name: "login" });
};
</script>