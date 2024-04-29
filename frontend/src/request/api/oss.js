import { useMyFetch } from "../useMyFetch";

const getDiskListAPI = () => {
	return useMyFetch("/user/oss-accounts").get().json();
};

const getObjectListAPI = (ossId, path) => {
	if (!path) {
		return useMyFetch(`/oss/${ossId}/list`).get().json();
	}
	return useMyFetch(`/oss/${ossId}/list?prefix=${path}`).get().json();
};

const getObjectDownloadUrlAPI = (ossId, objectKey) => {
	return useMyFetch(`/oss/${ossId}/object?object_key=${objectKey}&expires=3600`)
		.get()
		.json();
};

export { getDiskListAPI, getObjectListAPI, getObjectDownloadUrlAPI };
