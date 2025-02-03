from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.algorithm.function import solve_kmap


class SolveRequest(BaseModel):
    func: str


app = FastAPI(
    title="API для вычисления карты Карно 4x4",
    version="1.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    # Разрешить все методы (GET, POST, PUT, DELETE и т. д.)
    allow_methods=["*"],
    allow_headers=["*"],  # Разрешить все заголовки
)


@app.get("/")
async def root():
    return {"message": "From K-MAP API: Hello World!"}


@app.post("/solve-kmap/")
async def solve_kmap_api(data: SolveRequest):
    if len(data.func) != 16:
        return {"error": "The function must contain 16 characters"}
    elif not all(c in '01' for c in data.func):
        return {"error": "The function must contain only 0 and 1 characters"}
    return solve_kmap(data.func)
