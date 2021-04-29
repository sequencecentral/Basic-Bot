import os
from os import environ
import sys
import json
import random
try:
    #if run from inside of my module
    from . import sentiment
except:
    #if run standalone
    import sentiment

class Responder:
    def __init__(self,character='default'):
        self.character=character
        self.load_intros()
        self.load_replies()
        self.load_emojis()
        self.sen = sentiment.Sentiment_Analyzer()

    def load_intros(self):
        with open("""characters/{}.json""".format(self.character)) as f:
            self.intros = json.load(f)["retweet"]

    def load_replies(self):
        with open("""characters/{}.json""".format(self.character)) as f:
            self.replies = json.load(f)["reply"]

    def load_emojis(self):
        with open('emojis.json') as f:
            self.emojis = json.load(f)

    ################################# Intros #################################
    def get_random_intro(self):
        random_intro = random.choice(self.intros["neutral"])
        return random_intro

    def get_pos_intro(self):
        random_intro = random.choice(self.intros["positive"])
        return random_intro

    def get_neg_intro(self):
        random_intro = random.choice(self.intros["negative"])
        return random_intro
    
    #Intro has original text included
    def get_intro(self,text):
        sent = self.sen.get_sentiment(text).lower()
        print("Sentiment is: %s"% (sent))
        if 'positive' in sent:
            intro = """{}""".format(self.get_pos_intro()["content"])
        elif 'negative' in sent:
            intro = """{}""".format(self.get_neg_intro()["content"])
        else:
            intro = """{}""".format(self.get_random_intro()["content"])
        print("Intro: %s"%(intro))
        return intro

    ################################# Replies #################################
    def get_random_reply(self):
        random_reply = random.choice(self.replies["neutral"])
        return random_reply

    def get_pos_reply(self):
        random_reply = random.choice(self.replies["positive"])
        return random_reply

    def get_neg_reply(self):
        random_reply = random.choice(self.replies["negative"])
        return random_reply

    def get_reply(self,text):
        sent = self.sen.get_sentiment(text)
        if 'Positive' in sent:
            return """{} {} {} """.format(self.get_pos_emoji(),self.get_pos_reply()["content"],self.get_pos_emoji())
        elif 'Negative' in sent:
            return """{} {} """.format(self.get_neg_emoji(),self.get_neg_reply()["content"])
        else:
            return """{} {} {} """.format(self.get_random_emoji(),self.get_random_reply()["content"],self.get_random_emoji())

    ################################# Emojis #################################
    def get_random_emoji(self):
        return random.choice(self.emojis["neutral"])

    def get_pos_emoji(self):
        return random.choice(self.emojis["positive"])

    def get_neg_emoji(self):
        return random.choice(self.emojis["negative"])
    
    def get_emoji(self,text):
        sent = self.senself.sen.get_sentiment(text)
        emoji=''
        if 'Positive' in sent:
            emoji = self.get_pos_emoji()
        elif 'Negative' in sent:
            emoji = self.get_neg_emoji()
        else:
            emoji = self.get_random_emoji()
        return emoji
    