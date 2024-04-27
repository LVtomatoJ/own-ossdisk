import { createRouter, createWebHistory } from "vue-router";

import { useAuthStore } from "../store/auth.js";

import HomeView from "../view/HomeView.vue";
import LoginView from "../view/LoginView.vue";
import UserView from "../view/user/UserView.vue";
import UserHome from "../view/user/view/UserHome.vue";

const routes = [
	{ path: "/", component: HomeView, name: "home" },
	{ path: "/login", component: LoginView, name: "login" },
	{
		path: "/user",
		component: UserView,
		meta: { requiresAuth: true },
		children: [{ path: "", name: "user", component: UserHome }],
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

router.beforeEach((to, from) => {
	// instead of having to check every route record with
	// to.matched.some(record => record.meta.requiresAuth)
	if (to.meta.requiresAuth && !useAuthStore().isLoggedIn) {
		// this route requires auth, check if logged in
		// if not, redirect to login page.
		return {
			path: "/login",
			// save the location we were at to come back later
			query: { redirect: to.fullPath },
		};
	}
});

export default router;
