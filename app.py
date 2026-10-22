from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
import requests
import streamlit as st
from datetime import datetime, timezone
from sentiment_model import train_model, predict_sentiment

def fetch_auto_trends():
    import xml.etree.ElementTree as ET

    url = "https://news.google.com/rss"
    params = {
        "hl": "en-IN",
        "gl": "IN",
        "ceid": "IN:en"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        trends = []

        for item in root.findall(".//item")[:15]:
            title = item.findtext("title", "").strip()

            if title:
                trends.append(title)

        return trends

    except (requests.RequestException, ET.ParseError):
        return [] 
    
def fetch_trending_topics(topic):
    url = "https://news.google.com/rss/search"
    params = {
        "q": topic,
        "hl": "en-IN",
        "gl": "IN",
        "ceid": "IN:en"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.content)

        articles = []

        for item in root.findall(".//item")[:5]:
            title = item.findtext("title", "")
            if title:
                articles.append(title)

        return articles

    except (requests.RequestException, ET.ParseError):
        return []

def generate_post_drafts(headline, analyzed_posts):
    headline = headline.strip().rstrip(".")

    best_post = max(
        analyzed_posts,
        key=lambda p: p["likes"] + p["replies"],
        default=None
    )

    engagement_note = ""

    if best_post:
        engagement = best_post["likes"] + best_post["replies"]

        engagement_note = (
            f"\n\nYour highest-engagement post received "
            f"{best_post['likes']} likes and "
            f"{best_post['replies']} replies."
        )

    drafts = [
        {
            "style": "Insight-driven",
            "text": (
                f"An important development: {headline}.\n\n"
                "Beyond the immediate news, what does this mean "
                "for the people and systems affected by it?\n\n"
                "The real challenge is turning new developments "
                "into better decisions."
            )
        },
        {
            "style": "Discussion-driven",
            "text": (
                f"Let's examine this development: {headline}.\n\n"
                "What do you think is the biggest opportunity "
                "or risk here, and why?\n\n"
                "I'd like to hear thoughtful perspectives."
            )
        },
        {
            "style": "Concise opinion",
            "text": (
                f"{headline}.\n\n"
                "The headline matters, but the long-term "
                "consequences matter even more.\n\n"
                "What should we pay closest attention to next?"
            )
        }
    ]

    return drafts, engagement_note   
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
# Choose analysis mode
if "analysis_mode" not in st.session_state:
    st.session_state.analysis_mode = "Analyze by Username"

mode = st.radio(
    "Choose analysis mode:",
    ["Analyze by Username", "Analyze Individual Tweet"],
    key="analysis_mode",
    horizontal=True
)


# --------------------------------
# Mode 1: Analyze posts by username
# --------------------------------
if mode == "Analyze by Username":

    username = st.text_input(
        "Enter X username (without @)",
        placeholder="e.g. NASA"
    )

    if st.button("Fetch and Analyze Posts", type="primary"):

        if not username.strip():
            st.warning("Please enter a username.")

        else:
            url = (
                f"https://api.fxtwitter.com/"
                f"2/profile/{username.strip()}/statuses"
            )

            try:
                with st.spinner("Fetching posts..."):
                    response = requests.get(
                        url,
                        params={"count": 5},
                        timeout=20
                    )
                    response.raise_for_status()
                    data = response.json()

                posts = data.get("results", [])[:5]

                if not posts:
                    st.warning("No posts were returned for this username.")

                else:
                    analyzed_posts = []

                    for post in posts:
                        text = post.get("text", "").strip()

                        if not text:
                            continue

                        posted_at = post.get(
                            "created_at",
                            "Date unavailable"
                        )

                        try:
                            language = detect(text)
                        except LangDetectException:
                            language = "unknown"

                        prediction, confidence = predict_sentiment(
                            text, model, vectorizer
                        )

                        likes = post.get("likes", 0) or 0
                        replies = post.get("replies", 0) or 0

                        analyzed_posts.append({
                            "text": text,
                            "posted_at": posted_at,
                            "language": language,
                            "sentiment": prediction,
                            "confidence": confidence,
                            "likes": likes,
                            "replies": replies
                        })

                    # Save analysis results across Streamlit reruns
                    st.session_state["analyzed_posts"] = analyzed_posts
                    st.session_state.pop("topic_news", None)
                    st.session_state.pop("auto_trends", None)
                    st.session_state.pop("selected_topic", None)
                    st.session_state.pop("suggested_post", None)

            except requests.RequestException:
                st.error(
                    "Unable to fetch posts. Check the username "
                    "or try again later."
                )
            except (ValueError, TypeError):
                st.error("The server returned an unexpected response.")

    # Display saved posts independently of the Fetch button
    analyzed_posts = st.session_state.get("analyzed_posts", [])

    if analyzed_posts:

        for index, post in enumerate(analyzed_posts, start=1):

            with st.container(border=True):
                st.subheader(f"Post {index}")
                st.caption(f"📅 Posted: {post['posted_at']}")
                st.caption(
                    f"🌐 Detected language: {post['language'].upper()}"
                )
                st.write(post["text"])

                if post["language"] not in ("en", "unknown"):
                    if st.button(
                        "🌐 Translate to English",
                        key=f"translate_saved_{index}"
                    ):
                        try:
                            with st.spinner("Translating..."):
                                translated = GoogleTranslator(
                                    source="auto",
                                    target="en"
                                ).translate(post["text"])

                            st.info(translated)

                        except Exception:
                            st.error("Translation failed. Please try again.")

                col1, col2, col3 = st.columns(3)
                col1.metric("Likes", post["likes"])
                col2.metric("Replies", post["replies"])
                col3.metric("Sentiment", post["sentiment"])

                st.write(
                    f"Confidence: {post['confidence']:.2f}%"
                )

        positive_count = sum(
            p["sentiment"] == "Positive" for p in analyzed_posts
        )
        negative_count = sum(
            p["sentiment"] == "Negative" for p in analyzed_posts
        )
        total_engagement = sum(
            p["likes"] + p["replies"] for p in analyzed_posts
        )

        st.subheader("Sentiment Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Positive Posts", positive_count)
        col2.metric("Negative Posts", negative_count)
        col3.metric("Total Engagement", total_engagement)

        best_post = max(
            analyzed_posts,
            key=lambda p: p["likes"] + p["replies"]
        )

        st.subheader("⭐ Highest-Engagement Post")
        st.write(best_post["text"])
        st.caption(
            f"Likes: {best_post['likes']} | "
            f"Replies: {best_post['replies']}"
        )

    # --------------------------------
    # Trend-aware post recommendation
    # Keep this OUTSIDE the Fetch button
    # --------------------------------

    st.divider()
    st.subheader("🔥 Trend-Aware Post Recommendation")

    trend_mode = st.radio(
        "Choose how to find a topic:",
        ["Search Manually", "Auto-Detect Trends"],
        key="trend_mode",
        horizontal=True
    )

    if trend_mode == "Search Manually":

        topic = st.text_input(
            "Enter a topic",
            placeholder="e.g. Artificial Intelligence",
            key="manual_topic"
        )

        if st.button("Find Related News"):
            if not topic.strip():
                st.warning("Please enter a topic.")

            else:
                with st.spinner("Finding recent news..."):
                    news = fetch_trending_topics(topic.strip())

                if news:
                    st.session_state["topic_news"] = news
                    st.session_state["selected_topic"] = topic.strip()
                    st.session_state.pop("suggested_post", None)
                else:
                    st.session_state["topic_news"] = []
                    st.warning("No recent news found for this topic.")

        news = st.session_state.get("topic_news", [])

        if news:
            st.write("### 📰 Recent News")

            for headline in news:
                st.write(f"• {headline}")

    else:

        if st.button("Detect Trending Topics"):
            with st.spinner("Discovering current topics..."):
                trends = fetch_auto_trends()

            st.session_state["auto_trends"] = trends

            if trends:
                st.session_state.pop("suggested_post", None)
            else:
                st.warning("Unable to retrieve current news headlines.")

        trends = st.session_state.get("auto_trends", [])

        if trends:
            selected_trend = st.selectbox(
                "Select a topic from recent news:",
                trends,
                key="trend_selection"
            )

            st.session_state["selected_topic"] = selected_trend

            st.caption(
                "These are news headlines, not verified X trends."
            )


    # Generate and display post recommendations
    st.divider()
    st.subheader("✍️ Recommended Posts")

    if st.button("Generate 3 Post Ideas", type="primary"):
        if trend_mode == "Search Manually":
            topic = st.session_state.get("manual_topic", "").strip()
            news = st.session_state.get("topic_news", [])

            if not topic or not news:
                st.warning("Enter a topic and click Find Related News first.")
                st.stop()

            headline = news[0]

        else:
            trends = st.session_state.get("auto_trends", [])
            topic = st.session_state.get("trend_selection", "").strip()

            if not trends or not topic:
                st.warning("Click Detect Trending Topics and select a headline.")
                st.stop()

            headline = topic

        drafts, engagement_note = generate_post_drafts(
            headline,
            st.session_state.get("analyzed_posts", [])
        )

        st.session_state["recommended_drafts"] = drafts
        st.session_state["recommendation_headline"] = headline
        st.session_state.pop("suggested_post", None)

    drafts = st.session_state.get("recommended_drafts", [])

    if drafts:
        st.caption(
            f"Topic: {st.session_state.get('recommendation_headline', '')}"
        )

        for index, draft in enumerate(drafts):
            with st.container(border=True):
                st.subheader(draft["style"])
                st.write(draft["text"])

                st.text_area(
                    "Copy your preferred draft:",
                    value=draft["text"],
                    height=160,
                    key=f"draft_copy_{index}"
                )

        analyzed_posts = st.session_state.get("analyzed_posts", [])

        if analyzed_posts:
            best_post = max(
                analyzed_posts,
                key=lambda p: p["likes"] + p["replies"]
            )

            st.info(
                "Your highest-engagement post received "
                f"{best_post['likes']} likes and "
                f"{best_post['replies']} replies. "
                "Use this as a reference, not a guarantee of future engagement."
            )



    

# --------------------------------
# Mode 2: Analyze an individual tweet
# Keep your existing individual-tweet section here
# --------------------------------
else:
    # Keep your existing individual-tweet analysis code unchanged.
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

