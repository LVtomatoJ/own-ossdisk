import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../view/HomeView.vue";
import LoginView from "../view/LoginView.vue";

const routes = [
	{ path: "/", component: HomeView, name: "home" },
	{ path: "/login", component: LoginView, name: "login" },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
