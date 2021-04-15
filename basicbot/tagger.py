from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import pickle
import re, string, random

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

tags = {
    "5g":"#tech",
    "aws":"#cloud",
    "amazon":"#tech",
    "android":"#android",
    "apple":"#apple",
    "azure":"#cloud",
    "breach":"#cybersecurity",
    "bitcoin":"#crypto",
    "biology":"#science",
    "business":"#business",
    "cancer":"#science",
    "cell":"#cell",
    "change":"#tech",
    "cloud":"#cloud",
    "covid19":"#covid19",
    "crypto":"#crypto",
    "coin":"#crypto",
    "coinbase":"#crypto",
    "drug":"#health",
    "etherium":"#crypto",
    "exome":"#genomics",
    "facebook":"#tech",
    "fly":"#travel",
    "gadget":"#tech",
    "github":"#tech",
    "google":"#tech",
    "illumina":"#genomics",
    "internet":"#tech",
    "inovation":"#inovation",
    "iot":"#tech",
    "ios":"#apple",
    "iphone":"#apple",
    "tech":"#tech",
    "mac":"#tech",
    "macintosh":"#apple",
    "microsoft":"#tech",
    "mobile":"#mobile",
    "nature":"#science",
    "natera":"#genomics",
    "ngs":"#genomics",
    "personalis":"#genomics",
    "phone":"#tech",
    "privacy":"#cybersecurity",
    "quarantine":"#covid19",
    "reddit":"#tech",
    "selfie":"#selfie",
    "medicine":"#health",
    "mitosis":"#genomics",
    "musk":"#tech",
    "netflix":"#tech",
    "news":"#news",
    "records":"#cybersecurity",
    "replace":"#tech",
    "supplement":"#health",
    "food":"#food",
    "health":"#health",
    "tesla":"#tech",
    "travel":"#travel",
    "tourist":"#travel",
    "vacation":"#vacation",
    "vaccine":"#covid19",
    "vitamin":"#health",
    "virus":"#covid19",
    "wearable":"#tech",
    "work":"#business",
    "youtube":"#tech",
    "wgs":"#genomics",
}

def remove_noise(tweet_tokens):
    cleaned_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        token = re.sub(r'\W+', '', token).lower()
        if tag.startswith("NN"):
            pos = 'n' #noun
        elif tag.startswith('VB'):
            pos = 'v' #verb
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def tag_it(msg="",add_tags=""):
    words = remove_noise(msg.split(' '))
    #convert add_tags to string list
    at = add_tags.split(' ')
    # print(words)
    hashtags = {tags[word]:True for word in words if word in tags}
    for t in at:
        hashtags[t] = True
    if(len(hashtags)==0):
        return "#news"#default
    else:
        return ' '.join(hashtags.keys())

if __name__ == "__main__":
    msg = """ Newsweek 1995: "Why the Internet will Fail". health With Coinbase going public, many hit pieces will be written against Crypto. Stock brokers are already sending warn... https://newsweek.com/clifford-stoll-why-web-wont-be-nirvana-185306/ #tech #cybersecurity  #news
 """
    # h = tag_it("Wow! Mac is amazing!!! COVID19 this virus is crazy!!!")
    h = tag_it(msg,['#crypto','#science'])
    print(h)