def isPar(s):
    dic = {'}': '{', ')': '(', ']': '['}
    if len(s) == 0 or s[0] in dic.keys():
        return 'not Balanced'

    stack = []

    for char in s:
        if char in dic.values():
            stack.append(char)
        else:
            if stack:
                if dic[char] != stack.pop():
                    return 'not balanced'

    if stack:
        return 'not balanced'
    return 'balanced'


print(isPar('[({[([{}])]})]'))
