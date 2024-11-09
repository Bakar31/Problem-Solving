import string 
def isPalindrome(s: str) -> bool:
    punctuations = list(string.punctuation)
    s = ''.join(s.split(' '))
    s = ''.join([i for i in s if i not in punctuations]).lower()
    s_rev = ''.join([s[i] for i in range((len(s)-1), -1, -1)])
    
    if s == s_rev:
        return True
    else:
        return False


def is_palindrom2(s):
    for i in range(len(s)):
        s_list = list(s)
        s_list.remove(s[i])
        print(s_list)
        new_s = ''.join(s_list)
        if isPalindrome(new_s):
            return True
    return False


# s = "A man, a plan, a canal: Panama"
# res = isPalindrome(s)
# print(res)

# s = "race a car"
# res = isPalindrome(s)
# print(res)

s = "aba"
print(is_palindrom2(s))

s = "abca"
print(is_palindrom2(s))