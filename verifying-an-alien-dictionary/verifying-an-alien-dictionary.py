class Solution:
    def isAlienSorted(self, words, order):
        for i in range(len(words)-1):
            for j, (first, second) in enumerate(zip(words[i], words[i+1])):
                if order.index(first) > order.index(second): return False
                if order.index(first) < order.index(second): break
                if j == len(words[i+1])-1 and j != len(words[i])-1: return False
        return True