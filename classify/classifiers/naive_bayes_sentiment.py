'''

Uses naive Bayes to predict sentiment.

Training, test data format:
[ [ TEXT, SENTIMENT_SCORE] ... [TEXT, SENTIMENT_SCORE]

TODO: docs and docs and docs

'''
from abstract_classifier import Classifier
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class NaiveBayesSentiment(Classifier):
    # Compress a likert scale with 7 values to one with 3.
    @staticmethod
    def compress_likert(score):
        if score <= 3:
            return -1
        else if score == 4:
            return 0
        else:
            return 1

    @staticmethod
    def extract_docs_labels(examples):
        documents, labels = zip(*examples)
        labels = map(compress_likert, labels)
        return (documents, labels)

    def labels:
        return (-1, 0, 1)

    def train(self, training_examples):
        # Have: [ [Document, label], ... ]
        # Need: [[Features], ... ], [ label, ... ]
        documents, labels = get_docs_labels(training_examples)
        self.sentiment_clf = make_pipeline(
                HashingVectorizer(stop_words='english'), 
                MultinomialNB())

        # Map likert scale to -1, 0, 1 ...
        labels = map(compress_likert, labels)

        # Train!
        self.sentiment_clf.fit(documents, labels)

    def test(self, test_examples):
        documents, labels = get_docs_labels(test_examples)
        predictions = self.sentiment_clf.predict(documents)
        accuracy = np.mean(predictions == labels)
        return (zip(documents, predictions, labels), accuracy)