import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export interface Flight {
    id: number;
    origin: string;
    destination: string;
    status: string;
}

export interface TrajectoryPoint {
    lat: number;
    lon: number;
}

export const createFlight = async (origin: string, destination: string) => {
    const response = await axios.post<Flight>(`${API_BASE_URL}/flights/`, {
        origin,
        destination,
    });
    return response.data;
};

export const getFlightTrajectory = async (flightId: number) => {
    const response = await axios.get(
        `${API_BASE_URL}/flights/${flightId}/trajectory`
    );
    return response.data;
};
