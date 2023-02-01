#library for regular expressions
import re  
from html.parser import HTMLParser
import nltk
import itertools
from autocorrect import Speller
from nltk.corpus import stopwords

corpus = open("form_corpus.txt", "r")

corpus = HTMLParser().unescape(corpus)

encode_corpus =corpus.encode('ascii','ignore')
print("encode_corpus = \n{}".format(encode_corpus))
 
#decode from ascii to UTF-8
decode_corpus=encode_corpus.decode(encoding='UTF-8')
print("decode_corpus = \n{}".format(decode_corpus))

# remove hyperlinks
corpus = re.sub(r'https?:\/\/.\S+', "", corpus)
 
# remove hashtags
# only removing the hash # sign from the word
corpus = re.sub(r'#', '', corpus)
 
# remove old style recorpus text "RT"
corpus = re.sub(r'^RT[\s]+', '', corpus)

 #dictionary consisting of the contraction and the actual value
Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will",
           "'d":" would","'ve":" have","'re":" are"}
 
#replace the contractions
for key,value in Apos_dict.items():
    if key in corpus:
        corpus=corpus.replace(key,value)
        
#separate the words
corpus = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",corpus) if s])
print("After splitting attached words the corpus is:-\n{}".format(corpus))

corpus=corpus.lower()

#One letter in a word should not be present more than twice in continuation
corpus = ''.join(''.join(s)[:2] for _, s in itertools.groupby(corpus))
print("After standardizing the corpus is:-\n{}".format(corpus))
 
spell = Speller(lang='en')
#spell check
corpus=spell(corpus)
print("After Spell check the corpus is:-\n{}".format(corpus))

#download the stopwords from nltk using
nltk.download('stopwords')
#import stopwords
 
#import english stopwords list from nltk
stopwords_eng = stopwords.words('english')
 
corpus_tokens=corpus.split()
corpus_list=[]
#remove stopwords
for word in corpus_tokens:
    if word not in stopwords_eng:
        corpus_list.append(word)

#for string operations
import string         
clean_corpus=[]
#remove punctuations
for word in corpus_list:
    if word not in string.punctuation:
        clean_corpus.append(word)
 
