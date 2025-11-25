from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware

print("🚀 Loading models...")






# Load models
svm = joblib.load("svm_agnews_model.pkl")
embedder = SentenceTransformer("sentence_transformer_agnews")

# Category mapping
category_map = {
    1: 'World',
    2: 'Sports',
    3: 'Business',
    4: 'Sci/Tech'
}

# Initialize FastAPI
app = FastAPI(
    title="AG News Classifier API",
    description="Classifies news headlines into World, Sports, Business, or Sci/Tech using SentenceTransformer + SVM.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change "*" to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],          # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],          # Allows all headers including Authorization
)

# Request schema
class NewsItem(BaseModel):
    url: str

@app.get("/")
def root():
    return {"message": "AG News Classification API is running!"}

@app.post("/predict")
def predict_news(item: NewsItem):
    emb = embedder.encode([item.url])
    pred = svm.predict(emb)
    label = category_map[int(pred[0])]
    return {
        "predicted_category": label
    }
