from fastapi import FastAPI
from app.api.routes.players import router as players_router

app = FastAPI(title="Recall API")
app.include_router(players_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}