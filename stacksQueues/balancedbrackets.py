def isBalanced(s):
    new_list = []
    opening = "({["
    closing = ")}]"
    cmp_dict = {")":"(", "]":"[","}":"{"}
    if s[0] in closing:
        return "NO"
    for i in s:
        print('gotin')
        if i in opening:
            new_list.append(i)
        elif i in closing:
            if len(new_list) == 0:
                return "NO"
            elif cmp_dict[i] == new_list[-1]:
                new_list.pop()
            else:
                return "NO"
        else:
            return "NO"

    if len(new_list) == 0:
        return "YES"

    return "NO"