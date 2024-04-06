import { createFetch } from '@vueuse/core'
const useMyFetch = createFetch({
    baseUrl: 'http://127.0.0.1:8000',
    combination: 'overwrite',
    options: {
        // beforeFetch in pre-configured instance will only run when the newly spawned instance do not pass beforeFetch
        // async beforeFetch({ options }) {
        //     const myToken = await getMyToken()
        //     options.headers.Authorization = `Bearer ${myToken}`

        //     return { options }
        // },
    },
})
export { useMyFetch }