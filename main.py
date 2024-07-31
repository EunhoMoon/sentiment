import uvicorn
from fastapi import FastAPI

from app.api.analyze_api import analyze


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(analyze, prefix="/analyze", tags=["Analyze"])
    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", host="0.0.0.0", port=8000, reload=True, factory=True)
