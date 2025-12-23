<template>
    <div class="layout">
        <CreateFlightForm @flight-created="onFlightCreated" />
        <FlightMap :flightId="flightId" />
    </div>
</template>

<script setup lang="ts">
    import { ref } from "vue";
    import CreateFlightForm from "./components/CreateFlightForm.vue";
    import FlightMap from "./components/FlightMap.vue";

    const flightId = ref<number | null>(null);

    const onFlightCreated = (id: number) => {
        flightId.value = id;
    };
</script>

<style>
    html,
    body,
    #app {
        height: 100%;
        margin: 0;
    }

    .layout {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>

