'''
290. Word Pattern
'''

# Time Complexity : O(n) # n is the number of characters in the pattern and the number of words in the string s. We traverse both the pattern and the words once, so the time complexity is linear. O(1) for the dictionary operations since the maximum number of unique characters and words is limited (e.g., 26 for lowercase English letters).
# Space Complexity : O(1) # The space complexity is O(1) because the size of the mapping dictionaries is limited by the number of unique characters and words, which is constant (e.g., 26 for lowercase English letters). In practice, it can be considered O(1) since it does not grow with input size.
# Did this code successfully run on Leetcode : Yes, it passed all test cases.
# Any problem you faced while coding this : Yes, understanding the mapping of characters in the pattern to words in the string s and ensuring both mappings are consistent was a bit tricky at first.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: # humne ek function wordPattern banaya hai jo pattern aur string s ko input leta hai aur check karta hai ki kya pattern aur s ke words ka mapping sahi hai ya nahi (We have created a function wordPattern that takes a pattern and a string s as input and checks if the mapping of the pattern and the words in s is correct or not.)
        words = s.split() # yahan hum string s ko words mein split karte hain (Here we split the string s into words)
        if len(pattern) != len(words): # agar pattern aur words ki length alag hai to ye mapping sahi nahi ho sakti (if the lengths of the pattern and words are different, the mapping cannot be correct)
            return False # isiliye hum false return karte hain (so we return false)
        
        char_to_word = {} # yahaan hum ek dictionary hashmap banate hain jo pattern ke characters ko words se map karegi (Here we create a hash map that will map characters of the pattern to words)
        word_to_char = {} # yahaan hum ek aur dictionary hashmap banate hain jo words ko pattern ke characters se map karegi (Here we create another hash map that will map words to characters of the pattern)
        
        for char, word in zip(pattern, words): # is loop mein hum zip function ka use karte hain jo pattern ke characters aur words ko pair karta hai (In this loop, we use the zip function to pair characters of the pattern with words)
            '''Example of zip function:
            >>> pattern = "abba"
            >>> s = "dog cat cat dog"
            >>> words = s.split()  # words = ["dog", "cat", "cat", "dog"]
            >>> zip(pattern, words) will give us pairs: ('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')
            '''
            if char in char_to_word: # agar pattern ka character pehle se mapping mein hai (if the character from the pattern is already in the mapping)
                if char_to_word[char] != word: # to check karte hain ki kya ye character word se match karta hai (we check if it matches the corresponding word)
                    return False # agar match nahi karta to ye mapping sahi nahi hai (if it does not match, the mapping is incorrect)
            else: # agar pattern ka character pehle se mapping mein nahi hai (if the character from the pattern is not already in the mapping)
                char_to_word[char] = word # to hum is character ko word se map karte hain (we map it to the corresponding word)
            
            if word in word_to_char: # agar word pehle se mapping mein hai (if the word is already in the mapping)
                if word_to_char[word] != char: # to check karte hain ki kya ye word pattern ke character se match karta hai (we check if it matches the corresponding character in the pattern)
                    return False # agar match nahi karta to ye mapping sahi nahi hai (if it does not match, the mapping is incorrect)
            else: # agar word pehle se mapping mein nahi hai (if the word is not already in the mapping)
                word_to_char[word] = char # to hum is word ko pattern ke character se map karte hain (we map it to the corresponding character in the pattern)
        return True # agar humne saare characters aur words ko successfully map kar diya hai to ye mapping sahi hai (if we have successfully mapped all characters and words, the mapping is correct)