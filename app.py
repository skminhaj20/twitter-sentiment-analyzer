import streamlit as st
from sentiment_model import train_model, predict_sentiment

st.set_page_config(
page_title="Twitter Sentiment Analyzer",
page_icon="📊",
layout="centered"
)

st.title("🐦 Twitter Sentiment Analyzer")
st.write("Analyze the sentiment of your tweet using Machine Learning.")

@st.cache_resource
def load_model():
    return train_model()

model, vectorizer = load_model()

tweet = st.text_area(
"Enter your tweet:",
placeholder="Example: I absolutely love this product!",
height=120
)

if st.button("Analyze Sentiment", type="primary"):
    if not tweet.strip():
        st.warning("Please enter a tweet first.")
    else:
        prediction, confidence = predict_sentiment(
            tweet,
            model,
            vectorizer
        )

    st.subheader("Analysis Result")

    st.write(f"**Predicted Sentiment:** {prediction}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    st.progress(int(confidence))

    if prediction == "Positive":
        st.success("This tweet expresses positive sentiment! 😊")

    else:
        st.error("This tweet expresses negative sentiment. 😞")
