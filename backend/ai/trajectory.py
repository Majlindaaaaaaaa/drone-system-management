# app/ai/trajectory.py
from typing import List, Dict

CITY_COORDINATES = {
    "Prishtina": (42.6629, 21.1655),
    "Prizren": (42.2153, 20.7415),
    "Peja": (42.6591, 20.2883),
    "Gjakova": (42.3803, 20.4308),
}


def generate_ai_trajectory(origin: str, destination: str) -> List[Dict]:
    if origin not in CITY_COORDINATES or destination not in CITY_COORDINATES:
        return []

    lat1, lon1 = CITY_COORDINATES[origin]
    lat2, lon2 = CITY_COORDINATES[destination]

    steps = 6
    trajectory = []

    for i in range(steps + 1):
        trajectory.append({
            "lat": lat1 + (lat2 - lat1) * i / steps,
            "lon": lon1 + (lon2 - lon1) * i / steps
        })

    return trajectory
