import { defineStore } from 'pinia'
export const useUserStore = defineStore('user', () => {
    const token = ref('')
    const setToken = computed((newToken) => token.value = newToken)
    const getToken = computed(() => token.value)
})