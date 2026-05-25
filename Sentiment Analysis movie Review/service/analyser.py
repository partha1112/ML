import json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.models import load_model

class SentimentAnalyzer:
    def __init__(self):
        """Load tokenizer and model once during initialization"""
        with open("training/tokenizer.json") as f:
            self.tokenizer = tokenizer_from_json(f.read())
        self.model = load_model("training/model_2.keras")
    
    def predict(self, review):
        review_tr = pad_sequences(self.tokenizer.texts_to_sequences([review]), maxlen=200)
        response = self.model.predict(review_tr)
        
        # Extract scalar value from nested array
        score = response[0][0]
        
        # Determine sentiment
        sentiment = "Positive" if score >= 0.5 else "Negative"
        confidence = float(score)
        
        result = {
        "sentiment": sentiment,
        "confidence": round(confidence,2)
        }
        print(result)
        return result


# if __name__ == "__main__":
#     analyzer = SentimentAnalyzer()
#     analyzer.predict("The movie not bad. I was excited")