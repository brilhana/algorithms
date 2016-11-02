# Author: Alexandre Brilhante

''' Returns true if s is a palindrome. '''

def palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False
