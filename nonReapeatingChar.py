
'''
Given a string S consisting of lowercase Latin Letters, the task is to find the first non-repeating character in S.

Problem Link: https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

Input: “geeksforgeeks”
Output: f
Explanation: As 'f' is first character in the string which does not repeat.

'''



strng = 'geeksforgeeks'
index = 0
fnc = ''

def nonReapeatingChar(strng,index,fnc):
    if len(strng) == 0:
        print("Empty String")
    else:
        for char in strng:
            if strng.count(char) == 1:
                fnc += char
                break
            else:
                index += 1
        if index == len(strng):
            print("All characters are repeating")
        else:
            print("First non-repeating character is", fnc)
            
nonReapeatingChar(strng,index,fnc)
