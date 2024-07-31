from fastapi import APIRouter

from app.model import analyze_model

analyze = APIRouter()


@analyze.post("/")
async def get_sentiment(contents: str):
    if not contents:
        return {"error": "No contents provided."}
    analyze = analyze_model.Analyze()
    return analyze.analyze_sentiment_from_text(text_content=contents)


@analyze.get("/")
def index():
    return {"message": "Hello, Sentiment Analysis!"}
