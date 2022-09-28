def palindrome(str):
    new_str = ""
    rev_str = ""
    for char in str:
        if char.isalnum():
            new_str += char.lower()
    rev_str = new_str[::-1]
    return new_str == rev_str
    
    
print(palindrome("A man, a plan, a canal: Panama"))
print(palindrome("race a car"))
print(palindrome(""))
print(palindrome("*Q&#@%^*&^%#@!*%^!#*%^#@*!&%*^%&%#^"))
print(palindrome("1234567890"))
print(palindrome("135797531"))

#time complexity of the palindrome function is O(n) 
# because there is 1 for loop going through the initial string














