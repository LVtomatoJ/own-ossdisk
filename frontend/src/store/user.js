import { defineStore } from "pinia";

export const useUserStore = defineStore("user", () => {
	const token = ref("");
	const getToken = computed(() => token.value);
});
