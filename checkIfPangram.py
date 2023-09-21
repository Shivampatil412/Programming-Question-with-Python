
'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Problem Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/ 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
'''



sentence = 'qwertyuiopasdfghjklzxcvbnm'

def checkIfPangram(sentence):
    if sentence.isalpha() == True:
        return len(set(sentence))==26
    else:
        return False
    


print(checkIfPangram(sentence))