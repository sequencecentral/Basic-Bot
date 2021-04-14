from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import pickle
import re, string, random
from . import tools

#class-based version -- faster because model is stored
class Sentiment_Analyzer:
    def __init__(self,model_file = "naivebayes.pickle"):
        self.load_model(model_file)

    def load_model(self,model_file):
        classifier_f = open(model_file, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()

    def get_sentiment(self,custom_str=""):
        custom_tokens = tools.remove_noise(tools.word_tokenize(custom_str))
        sentiment = self.classifier.classify(dict([token, True] for token in custom_tokens))
        return sentiment

if __name__ == "__main__":
    print('sentiment analysis works')