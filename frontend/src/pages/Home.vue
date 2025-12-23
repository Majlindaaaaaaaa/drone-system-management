<template>
    <div style="display: flex; gap: 20px">
        <CreateFlightForm @flight-created="onFlightCreated" />
        <FlightMap :flightId="flightId" />
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CreateFlightForm from "../components/CreateFlightForm.vue";
import FlightMap from "../components/FlightMap.vue";

const flightId = ref<number | null>(null);

const onFlightCreated = (id: number) => {
  flightId.value = id;
};
</script>
