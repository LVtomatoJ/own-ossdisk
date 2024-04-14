<template>
      <div>
    <v-img
      class="mx-auto my-6"
      max-width="228"
      src=""
    ></v-img>

    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">账号</div>

      <v-text-field
        density="compact"
        placeholder="Username"
        prepend-inner-icon="mdi-account"
        variant="outlined"
        v-model="username"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        密码

        <a
          class="text-caption text-decoration-none text-blue"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Forgot login password?</a>
      </div>

      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
        v-model="password"
      ></v-text-field>
      <v-card
        class="mb-12"
        color="surface-variant"
        variant="tonal"
        v-if="loginError"
      >
        <v-card-text  class="text-medium-emphasis text-caption">
          {{ loginError.detail }}
        </v-card-text>
      </v-card>
      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
        @click = 'handleLogIn'
      >
        Log In
      </v-btn>

      <v-card-text class="text-center">
        <a
          class="text-blue text-decoration-none"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
import { loginAPI } from '../request/api/user';
import { ref } from 'vue'
const username = ref('')
const password = ref('')
const visible = ref(false)
const loginError = ref(null)
const handleLogIn = async () => {
  const { data, error } = await loginAPI(username.value, password.value)
  if (error.value != null) {
    console.error(error)
    loginError.value = error.value
  } else {
    loginError.value = null
    console.log(data)
  }
}

</script>