from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import ReviewRequest, PredictionResponse
from src.config import APP_NAME, VERSION, API_SECRET_KEY
from src.inference import SentimentAnalyzer

# Initialize analyzer instance
analyzer = SentimentAnalyzer()

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="IMDB Sentiment Analysis"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API key authentication
api_key_header = APIKeyHeader(name="X-API-key")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key

# Health check endpoint
@app.get("/", tags=["Health"], description="Endpoint for health check")
async def home(api_key: str = Depends(verify_api_key)):
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "status": "Ready to predict"
    }

# Prediction endpoint
@app.post("/predict", tags=["Prediction"], description="Sentiment Analysis Prediction", response_model=PredictionResponse)
async def predict_sentiment(request: ReviewRequest, api_key: str = Depends(verify_api_key)):
    try:
        sentiment, prob = analyzer.predict(request.text)
        return PredictionResponse(sentiment=sentiment, probability=prob)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There is an error in the model prediction: {str(e)}")