# Twitter Sentiment Analyzer

A machine learning project that analyzes tweet text and predicts whether its sentiment is **Positive or Negative** using Natural Language Processing (NLP) and machine learning.

## Current Features

* Load and explore tweet datasets using Pandas.
* Clean tweet text by removing URLs, usernames, punctuation, and extra spaces.
* Normalize repeated characters in words to improve text consistency.
* Convert text into numerical features using TF-IDF vectorization.
* Use unigrams and bigrams to capture individual words and word combinations.
* Train a Logistic Regression sentiment classification model.
* Evaluate model performance using accuracy, precision, recall, and F1-score.
* Inspect misclassified tweets to understand model errors.
* Analyze learned word weights to identify features associated with positive and negative sentiment.
* Predict sentiment for custom user-entered tweets.
* Display estimated prediction confidence.

## Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas
* **Machine Learning:** scikit-learn
* **Text Representation:** TF-IDF Vectorization
* **Classification Algorithm:** Logistic Regression
* **NLP:** Regular-expression-based text preprocessing

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

The reported accuracy is based on the current train-test split. Further evaluation and improvements are planned.

## Limitations

* The model predicts only Positive or Negative sentiment.
* Neutral sentiment is not supported by the current training dataset.
* Misspellings, sarcasm, and ambiguous text can lead to incorrect predictions.
* The model may struggle with context-dependent expressions and unfamiliar words.
* Prediction confidence is an estimated probability, not a guarantee of correctness.
* The model has been trained on a limited sample of the Sentiment140 dataset and may not generalize to every type of tweet.

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
* [ ] Further model evaluation and improvement
* [ ] Streamlit user interface
* [ ] X/Twitter data integration
* [ ] Audience feedback and trend analysis
* [ ] AI-generated post suggestions
* [ ] SQL-based history storage
* [ ] Testing and deployment

## Running the Project

1. Install Python and the required dependencies.

2. Place the Sentiment140 dataset file in the project directory.

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Enter a tweet when prompted to predict its sentiment.

6. Type `exit` to stop the program.

## Future Improvements

* Improve model performance through systematic evaluation and experimentation.
* Explore neutral sentiment classification.
* Build an interactive dashboard using Streamlit.
* Integrate X/Twitter data where API access and permissions permit.
* Analyze audience feedback, replies, and trending topics.
* Generate suggested posts based on sentiment analysis and audience feedback.
* Store analysis history in a SQL database.
* Test and deploy the application.

## Disclaimer

This project is for educational and portfolio purposes. Sentiment predictions are estimates and may not accurately reflect the intended meaning of every tweet.
