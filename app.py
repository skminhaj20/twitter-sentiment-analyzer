from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
import requests
import streamlit as st
from datetime import datetime, timezone
from sentiment_model import train_model, predict_sentiment

st.set_page_config(
    page_title="X Sentiment Analyzer",
    page_icon="📊",
    layout="centered"
)

st.title("𝕏 Sentiment Analyzer")
st.write("Analyze X posts using Machine Learning.")

@st.cache_resource
def load_model():
    return train_model()

model, vectorizer = load_model()

# Choose analysis mode
mode = st.radio(
    "Choose analysis mode:",
    ["Analyze by Username", "Analyze Individual Tweet"],
    horizontal=True
)

# --------------------------------
# Mode 1: Analyze posts by username
# --------------------------------
if mode == "Analyze by Username":

    username = st.text_input(
        "Enter X username (without @)",
        placeholder="e.g. narendramodi"
    )

    if st.button("Fetch and Analyze Posts", type="primary"):

        if not username.strip():
            st.warning("Please enter a username.")

        else:
            url = (
                "https://api.fxtwitter.com/"
                f"2/profile/{username.strip().lstrip('@')}/statuses"
            )

            try:
                with st.spinner("Fetching recent posts..."):
                    response = requests.get(
                        url,
                        params={"count": 20},
                        timeout=20
                    )
                    response.raise_for_status()
                    data = response.json()

                posts = data.get("results", [])

                # Sort posts newest first when timestamps are available.
                posts = sorted(
                    posts,
                    key=lambda p: p.get("created_timestamp", 0) or 0,
                    reverse=True
                )

                if not posts:
                    st.warning("No posts were returned for this username.")

                else:
                    analyzed_posts = []

                    for post in posts:
                        if len(analyzed_posts) >= 5:
                            break

                        text = post.get("text", "").strip()

                        if not text:
                            continue

                        # Detect language without excluding any posts.
                        try:
                            language = detect(text)
                        except LangDetectException:
                            language = "unknown"

                        prediction, confidence = predict_sentiment(
                            text, model, vectorizer
                        )

                        likes = post.get("likes", 0) or 0
                        replies = post.get("replies", 0) or 0
                        posted_at = post.get(
                            "created_at", "Date unavailable"
                        )

                        post_id = str(
                            post.get("id")
                            or post.get("url")
                            or len(analyzed_posts)
                        )

                        analyzed_posts.append({
                            "text": text,
                            "posted_at": posted_at,
                            "language": language,
                            "sentiment": prediction,
                            "confidence": confidence,
                            "likes": likes,
                            "replies": replies
                        })

                        with st.container(border=True):
                            st.subheader(
                                f"Post {len(analyzed_posts)}"
                            )

                            st.caption(f"📅 Posted: {posted_at}")
                            st.caption(
                                f"🌐 Detected language: {language.upper()}"
                            )

                            # Always show the original post.
                            st.write(text)

                            # Offer translation for non-English posts.
                            if language not in ("en", "unknown"):
                                if st.button(
                                    "🌐 Translate to English",
                                    key=f"translate_{post_id}"
                                ):
                                    try:
                                        with st.spinner("Translating..."):
                                            translated = GoogleTranslator(
                                                source="auto",
                                                target="en"
                                            ).translate(text)

                                        st.markdown("**English translation:**")
                                        st.info(translated)

                                    except Exception:
                                        st.error(
                                            "Translation failed. Please try again."
                                        )

                            col1, col2, col3 = st.columns(3)
                            col1.metric("Likes", likes)
                            col2.metric("Replies", replies)
                            col3.metric("Sentiment", prediction)

                            st.write(
                                f"Confidence: {confidence:.2f}%"
                            )

                    if analyzed_posts:
                        positive_count = sum(
                            p["sentiment"] == "Positive"
                            for p in analyzed_posts
                        )

                        negative_count = sum(
                            p["sentiment"] == "Negative"
                            for p in analyzed_posts
                        )

                        total_engagement = sum(
                            p["likes"] + p["replies"]
                            for p in analyzed_posts
                        )

                        st.subheader("Sentiment Summary")

                        col1, col2, col3 = st.columns(3)
                        col1.metric("Positive Posts", positive_count)
                        col2.metric("Negative Posts", negative_count)
                        col3.metric(
                            "Total Engagement", total_engagement
                        )

                        best_post = max(
                            analyzed_posts,
                            key=lambda p: p["likes"] + p["replies"]
                        )

                        st.subheader("Recommended Post Inspiration")

                        st.write(
                            "Your highest-engagement post can provide "
                            "inspiration for your next post."
                        )

                        st.info(best_post["text"])

                        st.caption(
                            "This recommendation uses past engagement "
                            "only. Live trends and actual reply texts "
                            "are not yet included."
                        )

            except requests.RequestException:
                st.error(
                    "Unable to fetch posts. Check the username or try again later."
                )

            except (ValueError, TypeError):
                st.error("The server returned an unexpected response.")

# --------------------------------
# Mode 2: Analyze an individual tweet
# --------------------------------
else:
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
                tweet, model, vectorizer
            )

            st.subheader("Analysis Result")
            st.write(f"**Predicted Sentiment:** {prediction}")
            st.write(f"**Confidence:** {confidence:.2f}%")
            st.progress(int(confidence))

            if prediction == "Positive":
                st.success("This tweet expresses positive sentiment! 😊")
            else:
                st.error("This tweet expresses negative sentiment. 😞")

