# app/models/flight.py
from pydantic import BaseModel
from typing import List, Dict


class FlightCreate(BaseModel):
    origin: str
    destination: str


class Flight(BaseModel):
    id: int
    origin: str
    destination: str
    status: str
    trajectory: List[Dict]
