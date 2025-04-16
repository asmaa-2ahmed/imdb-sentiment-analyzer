🎬 IMDB Sentiment Analyzer
An end-to-end movie review sentiment analysis web application using FastAPI, TensorFlow, and Streamlit. This tool classifies IMDB movie reviews as Positive or Negative with a confidence score.

📂 Project Structure
graphql
Copy
Edit
.
├── src/
│   ├── config.py              # Configuration constants and paths
│   ├── inference.py           # SentimentAnalyzer class for prediction
│   ├── schemas.py             # Pydantic models for API request/response
│   └── views/
│       └── custom_styles.css  # Custom Streamlit UI styling
├── main.py                    # FastAPI backend entry point
├── app.py                     # Streamlit frontend
├── assets/
│   ├── model.keras            # Trained Keras model
│   └── word2idx.joblib        # Vocabulary index
├── requirements.txt           # Project dependencies
└── README.md                  # You’re here!
🚀 Features
✅ Text preprocessing & tokenization

✅ Trained deep learning model (TensorFlow)

✅ REST API with FastAPI (secured with API key)

✅ Interactive UI with Streamlit

✅ Dynamic confidence visualization

✅ Custom dark theme with red accents

🛠️ Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/imdb-sentiment-analyzer.git
cd imdb-sentiment-analyzer
2. Create & activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up .env file
Create a .env file in the root directory with the following:

env
Copy
Edit
APP_NAME=IMDB Sentiment Analyzer
VERSION=1.0
API_SECRET_KEY=your_secure_api_key
Replace your_secure_api_key with a strong key.

🧠 Model Info
Architecture: Pre-trained Keras model

Input Length: 300 tokens

Embedding Size: 128

Vocabulary Size: 10,000

Trained on: IMDB Movie Reviews Dataset

▶️ Running the Application
Start the FastAPI Backend
bash
Copy
Edit
uvicorn main:app --reload
By default runs at: http://127.0.0.1:8000

Test health: GET / with header X-API-key: your_api_key

Swagger docs: http://127.0.0.1:8000/docs

Launch the Streamlit Frontend
bash
Copy
Edit
streamlit run app.py
Runs at: http://localhost:8501

Enter your API key to unlock features

Navigate through Home / Prediction / Model Info sections

🧪 Sample Reviews to Try
text
Copy
Edit
"This movie was absolutely fantastic! The acting was superb and the plot kept me engaged throughout."
→ Positive

"I found the film to be quite disappointing. The storyline was weak and the characters weren't developed."
→ Negative

"A masterpiece with brilliant cinematography and performances. Truly moving!"
→ Positive

"This film was boring and way too long. I almost fell asleep."
→ Negative
🔐 API Usage
🔑 Authentication
All endpoints require the header:

makefile
Copy
Edit
X-API-key: your_api_key
📤 POST /predict
Request Body:

json
Copy
Edit
{
  "text": "The movie was great and very emotional."
}
Response:

json
Copy
Edit
{
  "sentiment": "Positive",
  "probability": 0.93
}
