import subprocess
from .chat import *
from .sentiment import *
from .responder import *
from .tagger import *

import nltk
try:
    print("Downloading nltk data")
    nltk.download('wordnet')
    nltk.download('pros_cons')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
except Exception as e:
    print(e)

# print("Current directory: "+ strEXIT()
# t("ls")))
# try:
#     # from .tools import *
#     from .chat import *
#     from .sentiment import *
#     from .responder import *
# except:
#     print("Default imports failed for this configuration.")
#     # # from .tools import *
#     from seqbot.chat import *
#     from seqbot.sentiment import *
#     from seqbot.responder import *

# def converse():
#     c = nltk.chat.util.Chat(chat.pairs, nltk.chat.util.reflections)
#     c.converse()

# def get_chat():
#     return nltk.chat.util.Chat(chat.pairs, nltk.chat.util.reflections)

# def get_sentiment(custom_str=""):
#     return sentiment.get_sentiment(custom_str)