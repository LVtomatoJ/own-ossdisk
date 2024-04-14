import { useMyFetch } from '../useMyFetch';



const loginAPI = (username, password) => {
    return useMyFetch('/login').post({ username, password }).json();
}

export { loginAPI }