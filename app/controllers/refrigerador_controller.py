from fastapi import APIRouter
from app.models.electrodomestics import Refrigerador
from app.models.schemas import RefrigeradorSchema

router = APIRouter(
    prefix="/refrigerador",
    tags=["Refrigerador"]
)

@router.post("/")
def crear_refrigerador(refrigerador: RefrigeradorSchema):
    refrigerador_instancia = Refrigerador(refrigerador.marca, refrigerador.modelo, refrigerador.consumoEnergetico, refrigerador.tipo)
    return {"detalles": refrigerador_instancia.obtenerDetalles()}
