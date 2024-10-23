from pydantic import BaseModel

class LavadoraSchema(BaseModel):
    marca: str
    modelo: str
    consumoEnergetico: float
    capacidad: float

class RefrigeradorSchema(BaseModel):
    marca: str
    modelo: str
    consumoEnergetico: float
    tipo: str

class HornoSchema(BaseModel):
    marca: str
    modelo: str
    consumoEnergetico: float
    capacidad: float
