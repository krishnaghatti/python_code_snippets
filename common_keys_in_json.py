"""
this script loads all JSON files in the current directory and ranks the keys based on occurance
"""
from collections import Counter

result = Counter()
_, _, files = next(walk("./"))

for file in files:
    if filename.endswith('.json'):
        with open(file, 'r') as f:
            document =  json.loads(f.read())
            result += Counter(document.keys())
print(result.most_common())
