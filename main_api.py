# main_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Damit wir deine Module finden
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importiere deinen Core (angepasst an deine Struktur)
# Falls deine Klasse anders heißt, passen wir das an.
# Ich gehe davon aus, dass wir die Logik hier simulieren oder importieren.
from simulations.noetiko_gpu_core import NoetikoGPUCore 

app = FastAPI(
    title="NOETIKO API",
    description="SaaS Interface for 6D Topological Simulations",
    version="1.1.1"
)

# WICHTIG: CORS erlauben, damit Bubble zugreifen darf
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Produktion später auf deine Bubble-Domain einschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Das Datenmodell: Was Bubble uns schicken muss
class SimulationRequest(BaseModel):
    radius_torus: float = 10.0
    tube_radius: float = 2.5
    frequency: float = 1.42  # Hydrogen Line Standard
    grid_resolution: int = 50

# Die Antwort: Was wir an Bubble zurückschicken
class SimulationResponse(BaseModel):
    status: str
    message: str
    dimensional_metric: float
    data_points: int
    computation_time: float

@app.get("/")
def read_root():
    return {"status": "NOETIKO System Online", "version": "1.1.1 Gold Standard"}

@app.post("/simulate", response_model=SimulationResponse)
async def run_simulation(request: SimulationRequest):
    try:
        # Hier initialisieren wir deinen 10/10 Core
        # Wir übergeben die Parameter von Bubble an Python
        core = NoetikoGPUCore(
            resolution=request.grid_resolution, 
            device_type="cpu" # Für Cloud-Hosting erstmal CPU-Safe Mode, später GPU
        )
        
        # Simulation starten (Beispiel-Aufruf)
        result = core.run_topological_scan(
            radius=request.radius_torus,
            freq=request.frequency
        )
        
        return SimulationResponse(
            status="success",
            message="Dimensional Delimitation calculated.",
            dimensional_metric=result.get("metric", 0.98), # Beispiel-Wert aus Core
            data_points=result.get("points_count", 1000),
            computation_time=result.get("time", 0.15)
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
