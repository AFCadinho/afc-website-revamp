<script setup lang="ts">
import { ref } from 'vue';

const name = ref("");
const password = ref("");
const message = ref("");
const loading = ref(false);

const login = async () => {
  loading.value = true
  message.value = ""

  try {
    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      credentials: "include",
      body: JSON.stringify({
        name: name.value,
        password: password.value
      }),
    })

    const raw = await response.text()
    console.log("status:", response.status)
    console.log("raw response:", raw)

    let data: any = {}
    try {
      data = raw ? JSON.parse(raw) : {}
    } catch {
      message.value = `Expected JSON but got: ${raw}`
      return
    }

    if (!response.ok) {
      message.value = data.error || "Login failed"
      return
    }

    message.value = `Logged in as ${data.user.name}`
  } catch (error) {
    console.error(error)
    message.value = "Request failed before getting a valid response"
  } finally {
    loading.value = false
  }
}

const logout = async () => {
    loading.value = true;
    message.value = "";

    try {
        const response = await fetch("/api/auth/logout", {
            method: "POST",
            credentials: "include",
        });

        const data = await response.json();
        message.value = data.message;
    } catch (error) {
        console.error(error);
        message.value = "Logout failed";
    } finally {
        loading.value = false;
    }
};
</script>

<template>
    <div>
        <h2>Login Bro</h2>

        <form @submit.prevent="login">
            <div>
                <label>Name</label>
                <input type="text" placeholder="Username" v-model="name">
            </div>

            <div>
                <label>Password</label>
                <input type="password" placeholder="Password" v-model="password">   
            </div>

            <button type="submit" :disabled="loading">
                {{ loading ? "Loading..." : "Login" }}
            </button>

            <button type="button" @click="logout" :disabled="loading">
                Logout
            </button>
        </form>

        <p v-if="message">{{ message }}</p>
    </div>
</template>