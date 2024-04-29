<template>
    <div>
        <v-card>
            <v-card-title>
                <h1>Home</h1>
            </v-card-title>
            <v-card-text>
                <p>Welcome to the user home page</p>
            </v-card-text>
        </v-card>
        <!-- userinfo -->
        <v-card>
            <v-card-title>
                <h1>User Info</h1>
            </v-card-title>
            <v-card-text>
                <p>Family: {{ family }}</p>
                <p>Username: {{ username }}</p>
                <p>ID: {{ id }}</p>
            </v-card-text>
        </v-card>
        <DiskList />
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { userAPI } from "../../../request/api/user";
import DiskList from "../../../components/disk/DiskList.vue";
const family = ref("");
const id = ref("");
const username = ref("");


onMounted(async () => {
    const { data, error } = await userAPI();
    if (error.value != null) {
        console.error(error);
    } else {
        console.log(data.value)
        family.value = data.value.family;
        id.value = data.value.id;
        username.value = data.value.username;
    }
});



</script>