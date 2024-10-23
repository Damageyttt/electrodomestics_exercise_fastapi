from fastapi import FastAPI
from app.controllers import lavadora_controller, refrigerador_controller, horno_controller

app = FastAPI()

# Incluir los routers de cada tipo de electrodoméstico
app.include_router(lavadora_controller.router)
app.include_router(refrigerador_controller.router)
app.include_router(horno_controller.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Electrodomésticos"}
