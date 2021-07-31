from math import inf
from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            self.wordsDict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        
        min_dist = inf
        
        
        w1 = self.wordsDict[word1]
        w2 = self.wordsDict[word2]
        p1 = p2 = 0        
        
        while p1 < len(w1) and p2 < len(w2):
            min_dist = min(abs(w1[p1]-w2[p2]), min_dist)
            if w1[p1] < w2[p2]: p1+=1
            else: p2+=1
                    
        return min_dist
    
    


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)