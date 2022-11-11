import json
import sys
import nltk

if (len(sys.argv) != 2) : print("expecting 1 argument - text")
text = sys.argv[1]
tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
print(json.dumps(tagged))