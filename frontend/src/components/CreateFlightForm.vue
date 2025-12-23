<template>
    <div class="form-container">
        <h2>Create Flight</h2>

        <select v-model="origin">
            <option disabled value="">Select Origin</option>
            <option v-for="city in cities" :key="city" :value="city">
                {{ city }}
            </option>
        </select>

        <select v-model="destination">
            <option disabled value="">Select Destination</option>
            <option v-for="city in cities" :key="city" :value="city">
                {{ city }}
            </option>
        </select>

        <button @click="createFlight">Create Flight</button>
    </div>
</template>

<script setup lang="ts">
    import { ref } from "vue";
    import axios from "axios";

    const emit = defineEmits(["flight-created"]);

    const API_BASE = "http://127.0.0.1:8000";

    const cities = ["Prishtina", "Prizren", "Peja", "Gjakova"];

    const origin = ref("");
    const destination = ref("");

    const createFlight = async () => {
        if (!origin.value || !destination.value) {
            alert("Select origin and destination");
            return;
        }

        if (origin.value === destination.value) {
            alert("Origin and destination must be different");
            return;
        }

        const response = await axios.post(`${API_BASE}/flights/`, {
            origin: origin.value,
            destination: destination.value,
        });

        emit("flight-created", response.data.id);
    };
</script>

<style scoped>
    .form-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        width: 300px;
        padding: 20px;
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        margin-top: 20px;
    }

    select,
    button {
        padding: 10px;
        font-size: 14px;
    }

    button {
        background: #2563eb;
        color: white;
        border: none;
        cursor: pointer;
        border-radius: 6px;
    }

        button:hover {
            background: #1e40af;
        }
</style>

