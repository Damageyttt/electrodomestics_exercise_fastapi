from fastapi import APIRouter
from app.models.electrodomestics import Horno
from app.models.schemas import HornoSchema

router = APIRouter(
    prefix="/horno",
    tags=["Horno"]
)

@router.post("/")
def crear_horno(horno: HornoSchema):
    horno_instancia = Horno(horno.marca, horno.modelo, horno.consumoEnergetico, horno.capacidad)
    return {"detalles": horno_instancia.obtenerDetalles()}
