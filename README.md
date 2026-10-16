# Twitter Sentiment Analyzer

A machine learning project that analyzes tweet text and predicts whether its sentiment is Positive or Negative.

## Current Features

* Load and explore tweet datasets using Pandas.
* Clean text by removing URLs, usernames, punctuation, and extra spaces.
* Convert text into numerical features using TF-IDF.
* Train a Logistic Regression sentiment classification model.
* Evaluate model performance using accuracy, precision, recall, and F1-score.
* Predict sentiment for custom user-entered tweets.
* Display estimated prediction confidence.

## Tech Stack

* Python
* Pandas
* scikit-learn
* TF-IDF Vectorization
* Logistic Regression

## Dataset

This project uses a sample of the Sentiment140 dataset containing 20,000 tweets:

* 10,000 Negative tweets
* 10,000 Positive tweets

The full dataset is not included in this repository.

## Current Model Performance

* Training samples: 16,000
* Testing samples: 4,000
* Accuracy: 75.35%

These results represent the current baseline model. Further improvements are planned.

## Limitations

* The model predicts only Positive or Negative sentiment.
* Neutral sentiment is not supported by the current training dataset.
* Misspellings, sarcasm, and ambiguous text can produce incorrect predictions.
* Prediction confidence is an estimated probability, not a guarantee of correctness.

## Project Progress

* [x] Python basics and project setup
* [x] Dataset loading and exploration
* [x] Text preprocessing
* [x] TF-IDF feature extraction
* [x] Logistic Regression model training
* [x] Model evaluation
* [x] Custom tweet predictions
* [x] Prediction confidence
* [ ] Error analysis and model improvements
* [ ] Streamlit user interface
* [ ] X/Twitter data integration
* [ ] Audience feedback and trend analysis
* [ ] AI-generated post suggestions
* [ ] SQL-based history storage
* [ ] Testing and deployment

## Running the Project

1. Install the required dependencies.

2. Place the Sentiment140 dataset in the project directory.

3. Run:

   `python main.py`

4. Enter a tweet to predict its sentiment.

5. Type `exit` to stop.

## Future Improvements

* Improve model performance.
* Explore neutral sentiment classification.
* Build an interactive dashboard.
* Integrate X/Twitter data where API access permits.
* Analyze audience feedback and trends.
* Generate suggested posts based on sentiment analysis.
* Store analysis history in a database.
