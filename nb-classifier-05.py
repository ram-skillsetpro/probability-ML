# Naive Bayes Classifier
# Problem Statement:
#
# Use the "SMS Spam Collection" dataset to build a Naive Bayes classifier to classify SMS messages as spam or not spam.
# Dataset Link: SMS Spam Collection Dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
df = pd.read_csv(url, sep='\t', names=["label", "message"])

# Preprocess data
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.3, random_state=42)

# Vectorize text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Make predictions
y_pred = model.predict(X_test_vec)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Naive Bayes classifier: {accuracy}")

# Example prediction
new_email = ["Congratulations, claim your free prize now"]
new_email_transformed = vectorizer.transform(new_email)
prediction = model.predict(new_email_transformed)
print(f"Prediction: {'Spam' if prediction[0] == 1 else 'Not Spam'}")

