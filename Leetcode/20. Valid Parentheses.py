"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "{[]}"
Output: true

Input: s = "(]"
Output: false
"""

def isValid(s):

    s_list = [s[i:i+2] for i in range(0, len(s), 2)]
    checked = []

    for i, j in enumerate(s_list):
        print(i)
        if j == '()':
            checked.append('True')
        elif j == '{}':
            checked.append('True')
        elif j == '[]':
            checked.append('True')
        else:
            checked.append('False')

    print(checked)
    if set(checked) == {'True'}:
        return True
    else:
        return False


s = "(]"
state = isValid(s)
print(state)