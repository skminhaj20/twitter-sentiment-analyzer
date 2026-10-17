import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

columns = ["sentiment", "id", "date", "query", "username", "tweet"]

negative_df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None,
    names=columns,
    nrows=10000
)

positive_df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None,
    names=columns,
    skiprows=800000,
    nrows=10000
)

df = pd.concat([negative_df, positive_df], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df["sentiment"] = df["sentiment"].map({
    0: "Negative",
    4: "Positive"
})



def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\.\S+", "", tweet)
    tweet = re.sub(r"@\w+", "", tweet)
    tweet = re.sub(r"\s+", " ", tweet).strip()
    tweet = re.sub(r"#", "", tweet)
    tweet = re.sub(r"[^\w\s]", "", tweet)
    tweet = re.sub(r"(.)\1{2,}", r"\1\1", tweet)
    return tweet

df["cleaned_tweet"] = df["tweet"].apply(clean_tweet)

X = df["cleaned_tweet"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer(
    max_features=10000,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred,
    "Tweet": X_test
})

mistakes = results[results["Actual"] != results["Predicted"]]
print("Misclassified tweets:", len(mistakes))

print("\nExamples of misclassified tweets:")
print(mistakes.head(10))
print("\nRandom misclassified tweets:")
print(mistakes.sample(10, random_state=42))
feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

word_weights = pd.DataFrame({
    "Word": feature_names,
    "Weight": coefficients
})

print("\nWords associated with Positive sentiment:")
print(word_weights.sort_values("Weight", ascending=False).head(15))

print("\nWords associated with Negative sentiment:")
print(word_weights.sort_values("Weight").head(15))

while True:
    tweet = input("\nEnter a tweet (or type 'exit' to stop): ")

    if tweet.lower() == "exit":
        break

    cleaned = clean_tweet(tweet)
    tweet_tfidf = vectorizer.transform([cleaned])
    probabilities = model.predict_proba(tweet_tfidf)[0]

    prediction = model.classes_[probabilities.argmax()]
    confidence = probabilities.max() * 100

    print("Predicted sentiment:", prediction)
    print("Confidence:", round(confidence, 2), "%")