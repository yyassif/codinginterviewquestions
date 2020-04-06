#819. Most Common Word
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = ".,!?';:"
        for idx,para in enumerate(paragraph):
            if para in punc:
                paragraph = paragraph.replace(para," ")
        print(paragraph)
        arr = collections.Counter(paragraph.lower().split(" "))
        print(arr)
        most_freq = 0
        most_word = ''
        for word, freq in arr.items():
            if word !="" and word not in banned:
                if freq>most_freq:
                    most_freq = freq
                    most_word = word
        return most_word
        
