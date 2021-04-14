import nltk
import subprocess
from .chat import *
from .sentiment import *
from .responder import *
from .tagger import *

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