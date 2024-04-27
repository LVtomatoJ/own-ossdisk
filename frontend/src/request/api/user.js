import { useMyFetch } from "../useMyFetch";

const loginAPI = (username, password) => {
	return useMyFetch("/login").post({ username, password }).json();
};

const userAPI = () => {
	return useMyFetch("/user").get().json();
};

export { loginAPI, userAPI };
