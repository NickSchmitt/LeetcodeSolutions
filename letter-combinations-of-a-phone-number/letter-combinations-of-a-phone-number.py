phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        permutations = []
        if digits == "": return []
        def combine(position: int, string: str):
            if position == length:
                permutations.append(string)
            else:
                letters = phone[digits[position]]
                for letter in letters:
                    combine(position+1,string+letter)
        combine(0,"")
        return permutations