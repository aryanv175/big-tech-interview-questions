class Solution:
    def partitionString(self, s: str) -> int:
        count = 1 # we will always find atleast one substring so starting value of count should be 1
        substr = '' # this where we store our substrings
        for char in s:
            if char not in substr: # if a character is not present in the substring we add char to the substring
                substr += char
            else: 
                substr = char # now we form a new substring which is equal to the current char
                count += 1 # increase the count by 1
        return count # return count
