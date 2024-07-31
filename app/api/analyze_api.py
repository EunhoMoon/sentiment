from fastapi import APIRouter

from app import model

analyze = APIRouter()


@analyze.post("/")
async def get_sentiment(contents: str):
    if not contents:
        return {"error": "No contents provided."}
    return model.Analyze().analyze_sentiment_from_text(text_content=contents)


@analyze.get("/")
def index():
    return {"message": "Hello, Sentiment Analysis!"}
