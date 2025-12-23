def plan_trajectory(origin: str, destination: str):
    """
    Simulated trajectory planning logic.
    In real systems, this would include GIS data,
    obstacles, regulations, and optimization algorithms.
    """

    trajectory = {
        "origin": origin,
        "destination": destination,
        "waypoints": [
            f"{origin}-WP1",
            f"{origin}-WP2",
            f"{destination}"
        ],
        "risk_level": "low"
    }

    return trajectory
