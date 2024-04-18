import { createApp } from "vue";
import App from "./App.vue";

import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
// Vuetify
import "vuetify/styles";

// import 'material-design-icons-iconfont/dist/material-design-icons.css'
import "@mdi/font/css/materialdesignicons.css";
import { aliases, md } from "vuetify/iconsets/md";

const vuetify = createVuetify({
	components,
	directives,
	icons: {
		defaultSet: "mdi",
		aliases,
		sets: {
			md,
		},
	},
});

// Pinia
import { createPinia } from "pinia";
const pinia = createPinia();

// Vue Router
import router from "./router";

createApp(App).use(vuetify).use(pinia).use(router).mount("#app");
