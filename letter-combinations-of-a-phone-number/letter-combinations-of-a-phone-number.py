class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        dfs takes a path array and results array
            if the length of the path equals the length of the digits
                we've come up with a full permutation and can append it to the res arr and return
            
            next number is the index of digits equal to the current length of path 
            e.g. digits[1] for the 2nd number if path only has the 1st number, due to zero indexing
            
            iterate over the letters in this next number
                append it to the path
                call this recursive function on it
                after we recurse to the end of the permutation, we pop it off the path
        """
        KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        }
        if digits == "": return []
        def dfs(path, res):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            
            next_number = digits[len(path)]
            for letter in KEYBOARD[next_number]:
                path.append(letter)
                dfs(path, res)
                path.pop()
        
        res = []
        dfs([], res)
        return res
    
    