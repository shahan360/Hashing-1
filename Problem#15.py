'''
205. Isomorphic Strings
'''

# Time Complexity : O(n) # n is the length of the strings s and t. We traverse both strings once, so the time complexity is linear. O(1) for the dictionary operations since the maximum number of unique characters is limited (e.g., 26 for lowercase English letters).
# Space Complexity : O(1) # The space complexity is O(1) because the size of the mapping dictionaries is limited by the number of unique characters in the strings, which is constant (e.g., 26 for lowercase English letters). In practice, it can be considered O(1) since it does not grow with input size.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes, understanding the mapping of characters and ensuring both strings maintain the same character mapping was a bit tricky at first.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: # humne ek function isIsomorphic banaya hai jo do strings s aur t ko input leta hai aur check karta hai ki kya ye dono strings isomorphic hain ya nahi.(We have created a function isIsomorphic that takes two strings s and t as input and checks if these two strings are isomorphic or not.)
        if len(s) != len(t): # agar dono strings ki length alag hai to ye isomorphic nahi ho sakte (if the lengths of both strings are different, they cannot be isomorphic)
            return False # isiliye hum false return karte hain (so we return false)
        
        mapping_s_to_t = {} # yahan hum ek dictionary banate hain jo s ke characters ko t ke characters se map karegi (here we create a dictionary that will map characters of s to characters of t)
        mapping_t_to_s = {} # yahan hum ek aur dictionary banate hain jo t ke characters ko s ke characters se map karegi (here we create another dictionary that will map characters of t to characters of s)

        for char_s, char_t in zip(s, t): # is loop mein hum zip function ka use karte hain jo s aur t ke characters ko pair karta hai (in this loop, we use the zip function to pair characters of s and t)
            '''Example of zip function:
            s = "egg"
            t = "add"
            zip(s, t) will give us pairs: ('e', 'a'), ('g', 'd'), ('g', 'd')
            '''
            if char_s in mapping_s_to_t: # agar s ka character pehle se mapping mein hai (if the character from s is already in the mapping)
                if mapping_s_to_t[char_s] != char_t: # to check karte hain ki kya ye character t ke character se match karta hai (we check if it matches the corresponding character in t)
                    return False # agar match nahi karta to ye isomorphic nahi hain (if it does not match, they are not isomorphic)
            else: # agar s ka character pehle se mapping mein nahi hai (if the character from s is not already in the mapping)
                mapping_s_to_t[char_s] = char_t # to hum is character ko t ke character se map karte hain (we map it to the corresponding character in t)
            
            if char_t in mapping_t_to_s: # agar t ka character pehle se mapping mein hai (if the character from t is already in the mapping)
                if mapping_t_to_s[char_t] != char_s: # to check karte hain ki kya ye character s ke character se match karta hai (we check if it matches the corresponding character in s)
                    return False # agar match nahi karta to ye isomorphic nahi hain (if it does not match, they are not isomorphic)
            else: # agar t ka character pehle se mapping mein nahi hai (if the character from t is not already in the mapping)
                mapping_t_to_s[char_t] = char_s # to hum is character ko s ke character se map karte hain (we map it to the corresponding character in s)
        
        return True # agar humne saare characters ko successfully map kar diya hai to ye isomorphic hain (if we have successfully mapped all characters, they are isomorphic)