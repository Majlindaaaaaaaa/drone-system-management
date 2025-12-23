<template>
    <div id="map"></div>
</template>

<script setup lang="ts">
    import { onMounted, watch } from "vue";
    import L from "leaflet";
    import axios from "axios";

    const props = defineProps<{
        flightId: number | null;
    }>();

    let map: L.Map;
    let polyline: L.Polyline | null = null;

    const API_BASE = "http://127.0.0.1:8000";

    onMounted(() => {
        map = L.map("map").setView([42.6629, 21.1655], 8);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "© OpenStreetMap",
        }).addTo(map);
    });

    watch(
        () => props.flightId,
        async (id) => {
            if (!id) return;

            const res = await axios.get(
                `${API_BASE}/flights/${id}/trajectory`
            );

            const points = res.data.trajectory.map(
                (p: any) => [p.lat, p.lon]
            );

            if (polyline) {
                polyline.remove();
            }

            polyline = L.polyline(points, { weight: 4 }).addTo(map);
            map.fitBounds(polyline.getBounds());
        }
    );
</script>

<style scoped>
    #map {
        width: 90%;
        height: 500px;
        margin-top: 20px;
        border-radius: 8px;
    }
</style>
