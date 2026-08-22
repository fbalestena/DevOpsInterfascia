from fastapi import FastAPI

app = FastAPI(title="Interfascia Backend")


@app.get("/")
def inicio():
    return {
        "mensaje": "✅ Backend de Interfascia funcionando correctamente"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }