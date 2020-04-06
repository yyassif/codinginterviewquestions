#819. Most Common Word
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = "!?,';."
        for c in punc:
            paragraph = paragraph.replace(c," ")
        d = dict(Counter(paragraph.lower().split()))
        most_w,most_freq ='',-1
        for word,freq in d.items():
            if word not in banned:
                if freq>most_freq:
                    most_w = word
                    most_freq = freq
        return most_w
