from fastapi import FastAPI
from service.analyser import SentimentAnalyzer

api = FastAPI()
analyzer = SentimentAnalyzer()

@api.get("/classify")
def classify(review: str):
    return analyzer.predict(review)
