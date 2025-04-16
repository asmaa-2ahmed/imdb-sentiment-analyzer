import streamlit as st
import requests
import time

# Constants - Update these to match your FastAPI app
API_URL = "http://127.0.0.1:8000"  # Your FastAPI server address
# API_SECRET_KEY = API_SECRET_KEY     # Should match what's in your config.py

# Page Config
st.set_page_config(page_title="IMDB Sentiment Analyzer", page_icon="🎬", layout="wide")

# Load custom CSS for unique design
def load_custom_css():
    with open("src/views/custom_styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css()

# Title and Intro
st.markdown("<h1 style='text-align: center;'>🎬 IMDB Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze movie review sentiments with our pre-trained model 🍿</p>", unsafe_allow_html=True)
st.divider()

# Session state init
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False

# API Key Authentication
if not st.session_state.is_authenticated:
    with st.expander("🔑 Enter API Key to unlock features", expanded=True):
        api_key = st.text_input("API Key", type="password", placeholder="Paste your API key here...")

        def check_api_key(api_key):
            try:
                response = requests.get(
                    f"{API_URL}/",
                    headers={"X-API-key": api_key}
                )
                return response.status_code == 200
            except:
                return False

        if api_key:
            if check_api_key(api_key):
                st.session_state.is_authenticated = True
                st.session_state.api_key = api_key
                st.session_state.login_time = time.time()
                st.rerun()
            else:
                st.error("❌ Invalid API Key. Please double-check and try again.")
else:
    # Auto-hide success message after login
    if 'login_time' in st.session_state and time.time() - st.session_state.login_time < 5:
        success_box = st.empty()
        success_box.success("🎉 You're logged in!")
        time.sleep(1)
        success_box.empty()

# Main App Section
if st.session_state.is_authenticated:
    st.sidebar.title("🎬 Navigation")
    option = st.sidebar.radio("Choose a section", ["🏠 Home", "🔍 Make Prediction", "📊 Model Info"])

    # Home Section
    if option == "🏠 Home":
        st.header("📘 IMDB Review Sentiment Analysis")
        st.markdown("""
Welcome to the IMDB Sentiment Analysis tool! This application uses a pre-trained deep learning model 
to classify movie reviews as either **Positive** or **Negative**.

### How it works:
1. The model is a neural network trained on IMDB review data
2. It analyzes your text and predicts sentiment with confidence score
3. Built with TensorFlow/Keras for optimal performance

### Example reviews to try:
- "This movie was absolutely fantastic! The acting was superb and the plot kept me engaged throughout."
- "I found the film to be quite disappointing. The storyline was weak and the characters weren't developed."

Ready to analyze some reviews? Head over to the **Prediction** section!
        """)

    # In your streamlit.py, modify the prediction section (around line 100) to look like this:

    elif option == "🔍 Make Prediction":
        st.header("🔍 Review Sentiment Prediction")
        st.markdown("Enter a movie review text to analyze its sentiment:")
        
        input_text = st.text_area(
            "📝 Movie Review Text:", 
            placeholder="Paste or type a movie review here...",
            height=200
        )

        if st.button("🎬 Analyze Sentiment"):
            if not input_text.strip():
                st.warning("⚠️ Please enter some text to analyze")
            else:
                with st.spinner("🔍 Analyzing sentiment..."):
                    try:
                        response = requests.post(
                            f"{API_URL}/predict",
                            json={"text": input_text},
                            headers={"X-API-key": st.session_state.api_key}
                        )
                        
                        if response.status_code == 200:
                            prediction = response.json()
                            sentiment = prediction.get("sentiment", "Unknown")
                            probability = prediction.get("probability", 0.0)
                            
                            # Display results with appropriate styling
                            if sentiment == "Positive":
                                st.success(f"🎉 **Predicted Sentiment**: `{sentiment}`")
                                # Green progress bar for positive sentiment
                                st.markdown(
                                    f"""
                                    <style>
                                        .stProgress > div > div > div > div {{
                                            background-color: #4CAF50;  /* Green */
                                        }}
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                                )
                                st.progress(probability)
                            else:
                                st.error(f"😞 **Predicted Sentiment**: `{sentiment}`")
                                # Dark red progress bar for negative sentiment
                                st.markdown(
                                    f"""
                                    <style>
                                        .stProgress > div > div > div > div {{
                                            background-color: #8B0000;  /* Dark red */
                                        }}
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                                )
                                st.progress(probability)
                            
                            st.info(f"📊 **Confidence**: `{probability:.2%}`")
                            
                            # Show interpretation
                            if probability > 0.7:
                                st.markdown("**Interpretation**: Strong prediction")
                            elif probability > 0.6:
                                st.markdown("**Interpretation**: Moderate prediction")
                            else:
                                st.markdown("**Interpretation**: Weak prediction")
                        else:
                            st.error(f"❌ API Error: {response.json().get('detail')}")
                    except Exception as e:
                        st.error(f"🚨 Connection error: {str(e)}")
         # Model Info Section
    elif option == "📊 Model Info":
        st.header("📊 Model Information")
        
        with st.spinner("Fetching model details..."):
            try:
                response = requests.get(
                    f"{API_URL}/",
                    headers={"X-API-key": st.session_state.api_key}
                )
                
                if response.status_code == 200:
                    status = response.json()
                    st.success("✅ Model is ready for predictions!")
                    
                    cols = st.columns(2)
                    with cols[0]:
                        st.metric("Application", status['app_name'])
                    with cols[1]:
                        st.metric("Version", status['version'])
                    
                    st.markdown("### Model Details")
                    st.markdown("""
                            - **Model Type**: Neural Network (TensorFlow/Keras)
                            - **Classes**: Positive, Negative
                            - **Input Processing**: Text cleaning + word indexing
                            - **Architecture**: Pre-trained (loaded from model.keras)
                         """)
                else:
                    st.error(f"❌ Error fetching status: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"🚨 Connection error: {str(e)}")