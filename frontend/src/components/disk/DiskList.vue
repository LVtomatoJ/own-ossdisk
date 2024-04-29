<template>
    disk_list
    <v-list lines="one">
        <template v-for="disk in diskList" :key="disk.id">
            <v-list-item :title="disk.bucket_name" @click="showDiskObject(disk.id)" />
            <template v-if="disk.is_show">
                <ObjectList :diskId="disk.id" />
            </template>
        </template>
    </v-list>

</template>

<script setup>
import { ref, onMounted } from "vue";
import { getDiskListAPI } from "../../request/api/oss";
import ObjectList from "./ObjectList.vue";


const showDiskObject = async (id) => {
    diskList.value.find((disk) => {
        if (disk.id === id) {
            disk.is_show = !disk.is_show;
        }
    });
}

const diskList = ref([]);

const getDiskListData = async () => {
    const { data, error } = await getDiskListAPI();
    if (error.value != null) {
        console.error(error);
    } else {
        console.log(typeof data.value);
        console.log(data.value);
        diskList.value = data.value;
    }
};


onMounted(() => {
    getDiskListData();
});
</script>