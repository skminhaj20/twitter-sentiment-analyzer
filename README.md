# 𝕏 Sentiment Analyzer

A machine learning and NLP project that analyzes X (formerly Twitter) posts and predicts whether their sentiment is **Positive or Negative**. The application combines sentiment classification, public post retrieval, language detection, translation, engagement analysis, news discovery, and locally generated AI post recommendations in an interactive Streamlit interface.

The project uses **TF-IDF and Logistic Regression** for sentiment analysis and **Ollama with Llama 3.2** to generate three different post drafts based on a selected news headline.

## ✨ Features

### 1. Sentiment Analysis

* Load and explore tweet datasets using Pandas.
* Clean tweet text by removing URLs, usernames, punctuation, and extra spaces.
* Normalize repeated characters in words.
* Convert text into numerical features using TF-IDF.
* Train a Logistic Regression sentiment classification model.
* Evaluate the model using accuracy, precision, recall, and F1-score.
* Inspect misclassified tweets and learned word weights.
* Predict sentiment for individual user-entered tweets.
* Display an estimated prediction confidence.
* Cache the trained model in Streamlit to avoid unnecessary retraining during normal interactions.

### 2. X Username-Based Post Analysis

* Fetch recent public posts using the FxTwitter service.
* Analyze up to five posts returned by the application.
* Display each post in its original language.
* Detect the language of each post using Langdetect.
* Translate non-English posts into English using Deep Translator.
* Display posting dates and times when available.
* Show likes, replies, predicted sentiment, and confidence for each post.
* Summarize positive and negative posts.
* Calculate total engagement using likes and replies.
* Highlight the post with the highest combined likes and replies.

### 3. Individual Tweet Analysis

* Enter any tweet or text manually.
* Predict whether the text expresses Positive or Negative sentiment.
* Display the prediction confidence.
* Present the result through a progress bar and a status message.

### 4. News Discovery

The application provides two ways to discover topics for new posts.

**Manual Topic Search**

* Enter a topic, such as Artificial Intelligence.
* Retrieve recent related news headlines using Google News RSS.
* Select a headline as the subject for an AI-generated post.

**Automatic News Discovery**

* Retrieve recent headlines from Google News RSS.
* Display the available headlines in a selection menu.
* Select a headline to generate post ideas around its subject.

**Important:** Google News headlines represent news coverage, not verified X trending topics. This project does not claim to measure the number of X posts or unique users discussing a topic.

### 5. AI-Powered Post Recommendations

The application uses a locally running Ollama model to generate three different post drafts based on a selected news headline.

The three draft styles are:

* **Insight-driven:** Presents an observation or analysis of the selected topic.
* **Discussion-driven:** Encourages discussion through a relevant question or perspective.
* **Concise opinion:** Presents the topic through a short, opinion-oriented post.

The recommendation workflow:

1. Search for a topic or retrieve recent news headlines.
2. Select a relevant headline.
3. Send the headline and available recent post examples to the local AI model.
4. Generate three distinct post drafts.
5. Display the drafts in the Streamlit interface.
6. Copy a preferred draft for further editing.

When recent posts have been analyzed, their text, sentiment, likes, and replies can be included as context for the AI. The application also identifies the account's highest-engagement post as a reference.

The application uses Ollama locally, so the text-generation feature does not require a paid generative AI API.

**Limitations:**

* The AI may generate generic, inaccurate, or unsupported statements. Review every draft before publishing.
* Engagement information provides context, not proof of what will perform well in the future.
* The application does not guarantee increased engagement, positive sentiment, or viral reach.
* The selected news headline is the basis for the recommendation; this is not a comprehensive real-time X trend analysis.

### 6. Error Handling

* Handle failures when retrieving posts and news headlines.
* Handle translation failures.
* Display helpful messages when Ollama cannot be reached or returns an HTTP error.
* Handle invalid or incomplete AI-generated JSON.
* Preserve selected topics and generated recommendations across Streamlit interactions using session state.

## 🛠️ Tech Stack

| Technology          | Purpose                                                    |
| ------------------- | ---------------------------------------------------------- |
| Python              | Application development                                    |
| Pandas              | Dataset loading and exploration                            |
| Scikit-learn        | Machine learning and model evaluation                      |
| TF-IDF              | Text feature extraction                                    |
| Logistic Regression | Sentiment classification                                   |
| Streamlit           | Interactive web interface                                  |
| Requests            | HTTP requests to external services and the local AI API    |
| FxTwitter service   | Retrieving public profile posts and engagement information |
| Google News RSS     | Retrieving recent news headlines                           |
| Langdetect          | Automatic language detection                               |
| Deep Translator     | Translating posts into English                             |
| Ollama              | Running the local generative AI model                      |
| Llama 3.2 (3B)      | Generating post recommendations                            |

## 📊 Dataset and Model

The project uses a balanced sample of the Sentiment140 dataset containing **20,000 tweets**.

| Dataset Split |    Samples |
| ------------- | ---------: |
| Training      |     16,000 |
| Testing       |      4,000 |
| **Total**     | **20,000** |

The sample contains positive and negative tweets. Text preprocessing and TF-IDF feature extraction are used before training a Logistic Regression classifier.

### Model Evaluation

The current model has achieved approximately **76% accuracy** on the held-out test set in the recorded evaluation.

Actual results may vary depending on the dataset, preprocessing, and train-test split.

The model predicts Positive or Negative sentiment. It does not provide a separate Neutral class, and its confidence score should be treated as an estimate rather than a guarantee of correctness.

The full Sentiment140 dataset is not included in this repository because of its size. Obtain the dataset separately and place the required CSV file in the project directory before running the model-training workflow.

## 📁 Project Structure

```text
twitter_sentiment_analyzer/
│
├── app.py
├── main.py
├── sentiment_model.py
├── test_twitter.py
├── tweets.csv
├── requirements.txt
├── README.md
├── .gitignore
├── training.1600000.processed.noemoticon.csv  # Local dataset; not committed
└── venv/                                      # Local virtual environment
```

### File Descriptions

* **`app.py`** — Streamlit application, username analysis, individual tweet analysis, news discovery, and AI post recommendations.
* **`main.py`** — Main script for exploring and evaluating the sentiment analysis workflow.
* **`sentiment_model.py`** — Text preprocessing, model training, and sentiment prediction functions.
* **`test_twitter.py`** — Script for testing the retrieval of an individual X post.
* **`tweets.csv`** — Small sample dataset for development.
* **`requirements.txt`** — Python package dependencies.
* **`README.md`** — Project documentation.
* **`.gitignore`** — Excludes local files and other items that should not be committed.

The large Sentiment140 dataset and virtual environment should remain local and must not be uploaded to GitHub.

## 🚀 Installation and Setup

### Prerequisites

Install or prepare the following:

* Python
* Git
* Visual Studio Code or another Python editor
* Ollama for AI-powered post recommendations
* The required Sentiment140 dataset for model training

### Step 1: Clone the Repository

```bash
git clone https://github.com/skminhaj20/twitter-sentiment-analyzer.git
cd twitter-sentiment-analyzer
```

### Step 2: Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Prepare the Dataset

Obtain the Sentiment140 dataset separately and place the required file in the project directory.

The dataset is excluded from GitHub because of its size.

### Step 5: Install and Prepare Ollama

Install Ollama and download the required model:

```powershell
ollama pull llama3.2:3b
```

Confirm that the model is available:

```powershell
ollama list
```

The AI recommendation feature requires the local Ollama server to be running.

**Hardware note:** This project was tested on a Windows laptop where the model was successfully run using the CPU backend after encountering a GPU/CUDA compatibility issue. Performance depends on the available hardware.

## ▶️ Running the Application

### Step 1: Start Ollama

Open a terminal and run:

```powershell
ollama serve
```

Keep the terminal open.

If Ollama is already running, it may report that port `11434` is in use. In that case, do not start another server; check whether the existing server is responding.

### Step 2: Start Streamlit

Open a second terminal in the project directory.

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the application:

```powershell
streamlit run app.py
```

Streamlit will display a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

### Running AI Recommendations

To generate post ideas:

1. Open the username analysis mode.
2. Select **Search Manually** or **Auto-Detect Trends**.
3. Find news headlines and select a topic.
4. Click **Generate 3 Post Ideas**.
5. Review the three generated drafts.

The Ollama server must be accessible at `http://localhost:11434`.

If Ollama is unavailable, restart the server before using the AI recommendation feature.

## 🧪 Testing

Run the Python syntax check:

```powershell
python -m py_compile app.py main.py sentiment_model.py
```

Run the X post retrieval test:

```powershell
python test_twitter.py
```

The test script requests an X post ID as input.

The application should also be tested manually for:

* Individual tweet sentiment prediction.
* Username-based post retrieval and sentiment analysis.
* Language detection and translation.
* Sentiment and engagement summaries.
* Manual news-topic search.
* Automatic news headline retrieval.
* AI generation of three post drafts.
* Error handling when external services or Ollama are unavailable.

## ⚠️ Limitations

* Sentiment predictions are automated estimates and may not capture sarcasm, context, slang, or complex emotions.
* The classifier is trained for Positive and Negative sentiment; it does not identify Neutral sentiment as a separate class.
* The model was trained on English-language sentiment data. Predictions for other languages may be unreliable.
* Language detection may be inaccurate for short or mixed-language posts.
* The number and recency of retrieved posts depend on the external service.
* FxTwitter and Google News RSS are external services and may change or become unavailable.
* Translation depends on an external translation service.
* Google News headlines are not verified X trends.
* AI-generated drafts may contain inaccurate claims and should be reviewed before publication.
* Running a local language model requires additional system resources.
* The project does not currently include SQL-based analysis history, audience reply-text analysis, or a deployed public web application.

## 🔮 Future Improvements

* Improve sentiment classification and evaluation.
* Explore support for additional sentiment categories.
* Personalize AI-generated posts using historical sentiment and engagement patterns.
* Improve the grounding of generated posts in verified news information.
* Explore audience reply analysis using an accessible data source.
* Store analysis history using SQLite and SQL queries.
* Add historical sentiment dashboards and visualizations.
* Improve the user interface and accessibility.
* Add automated tests for the complete recommendation workflow.
* Deploy the application for public access.

## 📈 Project Progress

### Completed

* [x] Dataset loading and exploration
* [x] Text preprocessing
* [x] TF-IDF feature extraction
* [x] Logistic Regression model training
* [x] Model evaluation
* [x] Individual tweet sentiment prediction
* [x] Interactive Streamlit interface
* [x] Public X post retrieval by username
* [x] Language detection
* [x] English translation
* [x] Likes and replies display
* [x] Sentiment summary and engagement analysis
* [x] Manual news-topic search
* [x] Automatic news headline discovery
* [x] Local Ollama integration
* [x] Generation of three AI-powered post drafts
* [x] Error handling for AI generation failures
* [x] Testing of the main application workflows

### Future Work

* [ ] Improve sentiment model performance
* [ ] Improve AI recommendation quality and factual grounding
* [ ] Personalize recommendations using historical engagement patterns
* [ ] Analyze audience replies using an accessible data source
* [ ] Add SQLite-based analysis history
* [ ] Build historical sentiment dashboards
* [ ] Add more automated tests
* [ ] Deploy the application

## 📌 Disclaimer

This project is intended for educational and portfolio purposes.

Sentiment predictions are automated estimates and may not accurately reflect the intended meaning of every post. Post retrieval, news discovery, and translation depend on external services and their availability. AI-generated content may contain errors and should be reviewed before publication. The application does not guarantee increased engagement or positive audience sentiment.

