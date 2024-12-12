from fastapi import FastAPI
from controllers import router
from database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Registrar las rutas
app.include_router(router)

# Correr la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
