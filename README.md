# Twitter Sentiment Analyzer

A machine learning project that analyzes tweet text and predicts whether its sentiment is **Positive or Negative** using Natural Language Processing (NLP) and machine learning.

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
* Display sentiment results with colored messages and a confidence progress bar.
* Validate empty input before making predictions.
* Cache the trained model to avoid unnecessary retraining during normal Streamlit interactions.

## Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas
* **Machine Learning:** scikit-learn
* **Text Processing:** Regular Expressions
* **Feature Extraction:** TF-IDF Vectorization
* **Classification:** Logistic Regression
* **Frontend:** Streamlit

## Dataset

This project uses a sample of the Sentiment140 dataset containing **20,000 tweets**:

* 10,000 Negative tweets
* 10,000 Positive tweets

The dataset is divided into training and testing sets. The full dataset is not included in this repository.

## Current Model Performance

| Metric           |      Value |
| ---------------- | ---------: |
| Total tweets     |     20,000 |
| Training samples |     16,000 |
| Testing samples  |      4,000 |
| Accuracy         | **76.12%** |

The current model uses TF-IDF features with unigrams and bigrams, along with Logistic Regression.

These results are based on the current train-test split. Further evaluation and improvements are planned.

## Application Interface

The Streamlit application allows users to:

1. Enter a tweet into a text area.
2. Click the **Analyze Sentiment** button.
3. View the predicted Positive or Negative sentiment.
4. View the estimated prediction confidence.
5. See a confidence progress bar and a colored result message.

## Project Structure

```text
twitter_sentiment_analyzer/
├── app.py
├── main.py
├── sentiment_model.py
├── requirements.txt
├── README.md
├── tweets.csv
└── .gitignore
```

The Sentiment140 dataset must also be placed in the project directory to train the model locally. It is not included in the repository.

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/skminhaj20/twitter-sentiment-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd twitter-sentiment-analyzer
```

### 3. Create and activate a virtual environment (recommended)

On Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Add the dataset

Place `training.1600000.processed.noemoticon.csv` in the project directory.

The dataset must be obtained separately.

### 6. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal if your browser does not open automatically.

## Limitations

* The model predicts only Positive or Negative sentiment.
* Neutral sentiment is not supported by the current training dataset.
* Misspellings, sarcasm, and ambiguous text can lead to incorrect predictions.
* The model may struggle with context-dependent expressions and unfamiliar words.
* Prediction confidence is an estimated probability, not a guarantee of correctness.
* The model was trained on a limited sample of Sentiment140 and may not generalize to every type of tweet.
* The application currently analyzes manually entered text; live X/Twitter integration is not yet implemented.

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
* [ ] Further model evaluation and improvement
* [ ] X/Twitter data integration
* [ ] Audience feedback and trend analysis
* [ ] AI-generated post suggestions
* [ ] SQL-based history storage
* [ ] Testing and deployment

## Future Improvements

* Improve model performance through systematic evaluation.
* Explore neutral sentiment classification.
* Integrate X/Twitter data where API access and permissions permit.
* Analyze audience feedback, replies, and trending topics.
* Generate suggested posts based on sentiment analysis and audience feedback.
* Store analysis history in a SQL database.
* Add visualizations and analysis dashboards.
* Test and deploy the application.

## Disclaimer

This project is intended for educational and portfolio purposes. Sentiment predictions are estimates and may not accurately reflect the intended meaning of every tweet.
