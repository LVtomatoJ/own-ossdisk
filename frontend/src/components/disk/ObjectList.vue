<template>
    object_list
    disk_id:{{ diskId }}
    <v-list>
        <template v-for="object in objectList">
            <v-list-item @click="handleObject(object.key)" :title="object.key" />
        </template>
    </v-list>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getObjectListAPI, getObjectDownloadUrlAPI } from "../../request/api/oss";


const props = defineProps(["diskId"]);

const objectList = ref([]);

const getObjectListData = async () => {
    const { data, error } = await getObjectListAPI(props.diskId, '');
    if (error.value != null) {
        console.error(error);
    } else {
        console.log(data.value);
        objectList.value = data.value;
    }
};

const handleObject = async (key) => {
    const { data, error } = await getObjectDownloadUrlAPI(props.diskId, key)
    const downloadUrl = data.value;
    window.open(downloadUrl)
    console.log()
}

onMounted(() => {
    getObjectListData();
});

</script>
