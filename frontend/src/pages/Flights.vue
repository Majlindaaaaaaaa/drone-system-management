<template>
    <div class="container">
        <h1>Flights</h1>

        <form @submit.prevent="addFlight">
            <input v-model="newFlight.drone_id" placeholder="Drone ID" required />
            <input v-model="newFlight.origin" placeholder="Origin" required />
            <input v-model="newFlight.destination" placeholder="Destination" required />
            <button type="submit">Create Flight</button>
        </form>

        <ul>
            <li v-for="flight in flights" :key="flight.id">
                🚁 {{ flight.drone_id }} | {{ flight.origin }} → {{ flight.destination }} | {{ flight.status }}
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { getFlights, createFlight, Flight, FlightCreate } from "../api/flights";

const flights = ref<Flight[]>([]);

const newFlight = ref<FlightCreate>({
  drone_id: "",
  origin: "",
  destination: ""
});

const loadFlights = async () => {
  flights.value = await getFlights();
};

const addFlight = async () => {
  await createFlight(newFlight.value);
  newFlight.value = { drone_id: "", origin: "", destination: "" };
  loadFlights();
};

onMounted(loadFlights);
</script>

<style scoped>
    .container {
        max-width: 600px;
        margin: auto;
    }

    input {
        margin: 5px;
    }
</style>
