from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.flights import router as flights_router

app = FastAPI(
    title="Drone System Management - Kosovo",
    version="0.1.0",
    description="Platform for drone flight management (academic simulation)"
)

# ===============================
# CORS CONFIGURATION (FRONTEND)
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# ROUTES
# ===============================
app.include_router(flights_router)


# ===============================
# ROOT ENDPOINT (TEST)
# ===============================
@app.get("/")
def root():
    return {"status": "Backend is running 🚀"}
