import json
import sys
import nltk
from nltk.corpus import wordnet as wn

if (len(sys.argv) != 2) : print("expecting 1 argument - word")
word = sys.argv[1]
synsets = wn.synsets(word)
result = []

for synset in wn.synsets(word):
  #print(json.dumps(synset))
  #print(synset.definition())
  #print(synset.pos())
  result.append({ "definition": synset.definition(), "pos": synset.pos(), "examples": synset.examples() })
  # for example in synset.examples():
  #   print("  %s" %example);


print(json.dumps(result))



