'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Problem Link: https://leetcode.com/problems/defanging-an-ip-address/ 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''

def defangIPaddr(address):
    defanged_address = ""
    for char in address:
        if char == ".":
            defanged_address += "[.]"
        else:
            defanged_address += char
    return defanged_address

# Example usage:
address1 = "1.1.1.1"
address2 = "255.100.50.0"

defanged_address1 = defangIPaddr(address1)
defanged_address2 = defangIPaddr(address2)

print(defanged_address1)  # Output: "1[.]1[.]1[.]1"
print(defanged_address2)  # Output: "255[.]100[.]50[.]0"






