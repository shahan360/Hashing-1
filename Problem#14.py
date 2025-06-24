'''
49. Group Anagrams
'''

# Time Complexity : O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space Complexity : O(n * k) for storing the anagrams in a dictionary.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes, understanding how to use a dictionary to create hash maps for grouping anagrams.

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # humne ek function groupAnagrams banaya hai jo strs naam ke list ko input leta hai aur List[List[str]] return karta hai. (We have created a function groupAnagrams that takes a list called strs as input and returns a List of Lists of strings.)
        anagrams = {} # humne hash map banane ke liye ek dictionary anagrams initialize ki hai jo anagrams ko unke sorted key ke saath store karegi. (We have initialized a dictionary called anagrams to create a hash map that will store anagrams with their sorted keys.)
        for s in strs: # humne strs list ke har string element s ke upar loop chalaya hai check karne ke liye ki kya wo anagram hai. (We have looped through each string element s in the strs list to check if it is an anagram.)
            key = ''.join(sorted(s)) # humne har string s ko sort kiya aur uska key banaya jo anagrams ko identify karega. (We sorted each string s and created a key that will identify the anagrams.)
            if key not in anagrams: # agar upar banaya gaya key anagrams dictionary mein nahi hai, toh hum us key ke liye ek naya list initialize karte hain. (If the key created above is not in the anagrams dictionary, we initialize a new list for that key.)
                anagrams[key] = [] # humne anagrams dictionary mein key ke liye ek khali list banayi. (We created an empty list for the key in the anagrams dictionary.)
            anagrams[key].append(s) # humne string s ko anagrams dictionary ke key ke corresponding list mein append kiya. (We appended the string s to the list corresponding to the key in the anagrams dictionary.)

        return list(anagrams.values()) # humne anagrams dictionary ke values ko list mein convert karke return kiya. (We converted the values of the anagrams dictionary into a list and returned it.)