class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        zero_counter = 0
        max_zeroes = 0
        one_counter = 0
        max_ones = 0

        for i in s:
            if i == '0':
                one_counter = 0
                zero_counter += 1
                max_zeroes = max(zero_counter, max_zeroes)
            if i == '1':
                zero_counter = 0
                one_counter += 1
                max_ones = max(one_counter, max_ones)
        return max_ones > max_zeroes
