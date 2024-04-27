import { createFetch } from "@vueuse/core";
import { useAuthStore } from "../store/auth";
const useMyFetch = createFetch({
	baseUrl: "http://127.0.0.1:8000",
	combination: "overwrite",
	options: {
		// beforeFetch in pre-configured instance will only run when the newly spawned instance do not pass beforeFetch
		async beforeFetch({ options }) {
			options.headers.Authorization = useAuthStore().getToken;

			return { options };
		},
		onFetchError(ctx) {
			if (ctx.data) {
				ctx.error = ctx.data;
				return ctx;
			}
		},
	},
});
export { useMyFetch };
