import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
})

// Pinia
import { createPinia } from 'pinia'
const pinia = createPinia()

// Vue Router
import router from './router'


createApp(App).use(vuetify).use(pinia).use(router).mount('#app')
