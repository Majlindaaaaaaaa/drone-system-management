# app/routes/flights.py
from fastapi import APIRouter
from app.models.flight import FlightCreate, Flight
from ai.trajectory import generate_ai_trajectory

router = APIRouter(prefix="/flights", tags=["Flights"])

flights_db = {}
flight_counter = 1


@router.post("/")
def create_flight(flight: FlightCreate):
    global flight_counter
    
    trajectory = generate_ai_trajectory(
        flight.origin,
        flight.destination
    )

    new_flight = Flight(
        id=flight_counter,
        origin=flight.origin,
        destination=flight.destination,
        status="planned",
        trajectory=trajectory
    )

    flights_db[flight_counter] = new_flight
    flight_counter += 1

    return new_flight


@router.get("/{flight_id}/trajectory")
def get_flight_trajectory(flight_id: int):
    flight = flights_db.get(flight_id)

    if not flight:
        return {"error": "Flight not found"}

    return {
        "flight_id": flight.id,
        "origin": flight.origin,
        "destination": flight.destination,
        "trajectory": flight.trajectory
    }
