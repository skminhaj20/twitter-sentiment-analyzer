# 𝕏 Sentiment Analyzer

A machine learning project that analyzes X (formerly Twitter) posts and predicts whether their sentiment is **Positive or Negative** using Natural Language Processing (NLP) and machine learning. The application also supports username-based post retrieval, language detection, English translation, and engagement analysis through an interactive Streamlit interface.

## Current Features

* Load and explore tweet datasets using Pandas.
* Clean tweet text by removing URLs, usernames, punctuation, and extra spaces.
* Normalize repeated characters in words.
* Convert text into numerical features using TF-IDF vectorization.
* Use unigrams and bigrams to capture individual words and word combinations.
* Train a Logistic Regression sentiment classification model.
* Evaluate model performance using accuracy, precision, recall, and F1-score.
* Inspect misclassified tweets and analyze learned word weights.
* Predict sentiment for custom user-entered tweets.
* Display estimated prediction confidence.
* Provide an interactive web interface using Streamlit.
* Cache the trained model to avoid unnecessary retraining during normal Streamlit interactions.
* **Fetch recent posts by X username** using the FxTwitter service.
* **Display posts in their original language** without excluding non-English posts.
* **Detect the language** of each retrieved post.
* **Translate non-English posts into English** using an individual translation button.
* Display each post's date and time.
* Show likes, replies, sentiment, and confidence for each post.
* Summarize positive and negative posts and total engagement.
* Highlight the post with the highest combined likes and replies as inspiration for future content.

## Tech Stack

| Technology           | Purpose                                             |
| -------------------- | --------------------------------------------------- |
| Python               | Core programming language                           |
| Pandas               | Dataset loading and processing                      |
| scikit-learn         | Machine learning and model evaluation               |
| Regular Expressions  | Text cleaning and preprocessing                     |
| TF-IDF Vectorization | Text feature extraction                             |
| Logistic Regression  | Sentiment classification                            |
| Streamlit            | Interactive web interface                           |
| Requests             | HTTP requests for retrieving posts                  |
| FxTwitter API        | Retrieving public profile posts and engagement data |
| Langdetect           | Automatic language detection                        |
| Deep Translator      | Translating posts into English                      |

## Dataset

This project uses a balanced sample of the Sentiment140 dataset containing **20,000 tweets**:

* 10,000 negative tweets
* 10,000 positive tweets

The dataset is divided into training and testing sets:

* Training samples: 16,000
* Testing samples: 4,000

The full dataset is not included in this repository because of its size. It must be obtained separately and placed in the project directory for local model training.

## Current Model Performance

| Metric           |      Value |
| ---------------- | ---------: |
| Total tweets     |     20,000 |
| Training samples |     16,000 |
| Testing samples  |      4,000 |
| Accuracy         | **76.12%** |

The current model uses TF-IDF features with unigrams and bigrams, along with Logistic Regression.

These results are based on the current train-test split. Further evaluation and improvements are planned.

**Note:** The model predicts only Positive or Negative sentiment. Its predictions may be less reliable for non-English posts because the training data primarily contains English-language tweets.

## Application Interface

The Streamlit application provides two analysis modes.

### 1. Analyze by Username

1. Enter a public X username, such as `narendramodi`.
2. Fetch the available recent posts returned by the external service.
3. View each post in its original language.
4. View the detected language and posting date.
5. Click **Translate to English** for a detected non-English post.
6. View likes, replies, predicted sentiment, and confidence.
7. Review the sentiment summary and total engagement.
8. See the post with the highest combined likes and replies as inspiration for future content.

The application displays up to five posts from the posts returned by the service. The actual number and recency of posts depend on the data available from the external service.

### 2. Analyze Individual Tweet

1. Enter a tweet into the text area.
2. Click **Analyze Sentiment**.
3. View the predicted Positive or Negative sentiment.
4. View the estimated prediction confidence.
5. See the result displayed through a progress bar and colored message.

## Project Structure

```text
twitter_sentiment_analyzer/
│
├── app.py
├── main.py
├── sentiment_model.py
├── requirements.txt
├── README.md
├── tweets.csv
└── .gitignore
```

The Sentiment140 training dataset must also be placed in the project directory. It is not included in the repository.

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/skminhaj20/twitter-sentiment-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd twitter-sentiment-analyzer
```

### 3. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file should include:

```text
pandas==3.0.6
scikit-learn==1.9.1
streamlit==1.66.0
requests
langdetect
deep-translator
```

### 5. Add the dataset

Place `training.1600000.processed.noemoticon.csv` in the project directory.

The dataset must be obtained separately.

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal if your browser does not open automatically.

## Limitations

* The model predicts only Positive or Negative sentiment.
* Neutral sentiment is not supported by the current training dataset.
* Misspellings, sarcasm, and ambiguous text can lead to incorrect predictions.
* The model may struggle with context-dependent expressions and unfamiliar words.
* The model is trained primarily on English-language data, so predictions for other languages may be unreliable.
* Prediction confidence is an estimate derived from the model and is not a guarantee of correctness.
* The model was trained on a limited sample of Sentiment140 and may not generalize to every type of post.
* Post retrieval depends on the availability and behavior of the external FxTwitter service.
* The number and recency of retrieved posts depend on the posts returned by the service.
* Language detection may be inaccurate for short or mixed-language text.
* Translation depends on the availability of the external translation service.
* The current recommendation highlights the post with the highest combined likes and replies. It does not yet generate a new post using live trends or audience reply text.
* Live trend analysis, audience reply-text analysis, SQL-based history storage, and deployment have not yet been implemented.

## Project Progress

* [x] Python basics and project setup
* [x] Dataset loading and exploration
* [x] Text preprocessing
* [x] TF-IDF feature extraction
* [x] Logistic Regression model training
* [x] Model evaluation
* [x] Custom tweet predictions
* [x] Prediction confidence
* [x] Error analysis and initial model improvements
* [x] Streamlit user interface
* [x] X username-based post retrieval
* [x] Multilingual post display and language detection
* [x] English translation for non-English posts
* [x] Posting date and engagement metrics
* [x] Sentiment summary and engagement-based post inspiration
* [ ] Further model evaluation and improvement
* [ ] Live trending-topic analysis
* [ ] Audience reply-text analysis
* [ ] AI-generated post suggestions based on trends and audience feedback
* [ ] SQL-based analysis history
* [ ] Testing and deployment

## Future Improvements

* Improve model performance through systematic evaluation.
* Explore neutral sentiment classification.
* Improve sentiment analysis for multilingual content.
* Integrate reliable sources for current trending topics.
* Analyze audience replies when a reliable, accessible source is available.
* Generate suggested posts using sentiment, engagement, trends, and audience feedback.
* Store analysis history in a SQL database.
* Add visualizations and historical sentiment dashboards.
* Test and deploy the application.

## Disclaimer

This project is intended for educational and portfolio purposes. Sentiment predictions are automated estimates and may not accurately reflect the intended meaning of every post. Post retrieval and translation depend on external services and their availability.
