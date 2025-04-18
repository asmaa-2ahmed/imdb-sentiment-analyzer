# 🎬 IMDB Sentiment Analyzer

Welcome to the **IMDB Sentiment Analyzer**, a full-stack web application designed to classify movie reviews as **Positive** or **Negative** using deep learning. Built using **TensorFlow**, **FastAPI**, and **Streamlit**, this tool provides both a REST API and an interactive UI for real-time sentiment prediction.

Whether you're a developer, data scientist, or just a movie buff, this app lets you explore natural language processing and neural networks in action — all from your local machine!

---

## 🌟 Key Features

- ✅ **Real-time Sentiment Classification** using a trained Keras model  
- ✅ **Confidence Score Visualization** for transparency in predictions  
- ✅ **RESTful API** secured with an API key using FastAPI  
- ✅ **Interactive Frontend** powered by Streamlit  
- ✅ **Custom Themed UI** with dark mode and red accents  
- ✅ **Clean, modular codebase** ready for extension and experimentation  

---

## 🚀 Installation & Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/asmaa-2ahmed/imdb-sentiment-analyzer
cd imdb-sentiment-analyzer
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
```

### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```
APP_NAME=IMDB Sentiment Analyzer
VERSION=1.0
API_SECRET_KEY=your_secure_api_key
```
> 🔐 Replace `your_secure_api_key` with a strong secret key of your choice.

---

## ▶️ Running the Application Locally

### ✅ Start the FastAPI Backend (API)
```bash
uvicorn main:app --reload
```
- Runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Health Check: `GET /` with header `X-API-key: your_api_key`

---

### ✅ Launch the Streamlit Frontend (UI)
```bash
streamlit run app.py
```
- Runs at: [http://localhost:8501](http://localhost:8501)  
- Navigate through `Home`, `Prediction`, and `Model Info` sections  
- Enter your API key to unlock prediction functionality

---

## 🧠 Model Details

- **Architecture:** Pre-trained Keras Sequential model  
- **Input Length:** 300 tokens  
- **Embedding Size:** 128  
- **Vocabulary Size:** 10,000  
- **Dataset:** IMDB Movie Reviews (binary classification)

---

## 🧪 Example Reviews to Try

Here are some review texts you can use for testing:

| Sample Review                                                                                   | Expected Sentiment |
|--------------------------------------------------------------------------------------------------|---------------------|
| "This movie was absolutely fantastic! The acting was superb and the plot kept me engaged."       | 👍 Positive          |
| "I found the film to be quite disappointing. The storyline was weak and characters underdeveloped." | 👎 Negative       |
| "A masterpiece with brilliant cinematography and powerful performances. Truly moving!"           | 👍 Positive          |
| "This film was boring and way too long. I nearly fell asleep watching it."                       | 👎 Negative          |

---

## ⚙️ How It Works

1. **Text Input:** Users submit a review through the API or UI.
2. **Preprocessing:** The review is tokenized and padded to match the model’s input format.
3. **Model Inference:** The model predicts sentiment and outputs a probability score.
4. **Response Generation:** FastAPI returns the result as structured JSON.
5. **Visualization:** Streamlit displays the sentiment and confidence level in a clean interface.

---

## 🙋‍♂️ Want to Contribute?

We’d love your input! If you have:

- 🔧 Feature suggestions  
- 🐞 Bug reports  
- 🎨 UI/UX improvements  
- 🧪 Model performance tweaks  

Feel free to [open an issue](https://github.com/asmaa-2ahmed/imdb-sentiment-analyzer) or submit a pull request. Your feedback helps make this project even better!

---

## ⭐ Show Some Love

If you find this project helpful or interesting, consider giving it a **⭐ on GitHub** — it really helps!

---

## 📫 Stay Connected

Feel free to reach out via [GitHub Issues](https://github.com/asmaa-2ahmed/imdb-sentiment-analyzer) for questions or collaboration ideas.
