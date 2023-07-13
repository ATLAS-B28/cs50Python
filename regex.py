import re
from collections import Counter

def most_occur_ele(word):
    arr = re.findall(r'[0-9]+',word)
    maxm = 0
    max_ele = 0
    c = Counter(arr)
    for x in list(c.keys()):
        if c[x]>=maxm:
            maxm = c[x]
            max_ele = int(x)

    return max_ele

if __name__ == "__main__":
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occur_ele(word))