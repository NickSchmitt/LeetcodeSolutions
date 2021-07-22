class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        
        for i in logs:
            if i.split(" ")[1].isdigit(): 
                digits.append(i)
            else: 
                letters.append(i)
        
        for i in range(len(letters)):
            (idx, *contents) = letters[i].split(' ')
            letters[i] = (idx, " ".join(contents))
        
        print(f'letters: {letters}')
        letters.sort(key=lambda x: (x[1], x[0]))
        print(f'letters: {letters}')
        letters = list(map(lambda x: " ".join(x), letters))
        
        return letters + digits
        print(f'letters: {letters}')
        # letters.sort(key=lambda x: x[0])
        
        # print(letters+digits)
        
        # return letters + digits
        # iterate over logs
        
        # if logs[i].beginsWith dig, push to new digit list
        # else push to new letter list
        
        # sort the letter list by the number after "let"
        # if logs[i].startswith("dig"): return "dig"