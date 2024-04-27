import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useAuthStore = defineStore("user", () => {
	const accessToken = ref("");
	const tokenType = ref("");
	const getToken = computed(() => `${tokenType.value} ${accessToken.value}`);
	const isLoggedIn = computed(() => !!accessToken.value);
	const setToken = (token, token_type) => {
		accessToken.value = token;
		tokenType.value = token_type;
	};
	return {
		getToken,
		setToken,
		isLoggedIn,
	};
});
