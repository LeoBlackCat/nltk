from g2p_en import G2p
import json
import sys

if (len(sys.argv) != 2) : print("expecting 1 argument - text")
text = sys.argv[1]

texts = text.split()
g2p = G2p()
result = [];
for text in texts:
    out = g2p(text)
    result.append(out)

print(json.dumps(result))