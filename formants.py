import sys
import json
import praat_formants_python as pfp

if (len(sys.argv) != 2) : print("expecting 1 argument - filename")
filename = sys.argv[1]

result = pfp.formants_at_time(filename, 0)
print(result[0], result[1], result[2])