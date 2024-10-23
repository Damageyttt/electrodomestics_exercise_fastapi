from fastapi import APIRouter
from app.models.electrodomestics import Lavadora
from app.models.schemas import LavadoraSchema

router = APIRouter(
    prefix="/lavadora",
    tags=["Lavadora"]
)

@router.post("/")
def crear_lavadora(lavadora: LavadoraSchema):
    lavadora_instancia = Lavadora(lavadora.marca, lavadora.modelo, lavadora.consumoEnergetico, lavadora.capacidad)
    return {"detalles": lavadora_instancia.obtenerDetalles()}
