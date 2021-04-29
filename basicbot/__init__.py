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
