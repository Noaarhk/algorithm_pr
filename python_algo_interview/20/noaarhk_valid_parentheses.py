def isValid(s:str) -> bool:
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'[',
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


def isValid_2(s: str) -> bool:
    pair = dict(zip(list(')]}'), list('([{')))
    st = []
    for b in s:
        if b not in pair:
            st.append(b)
        elif not st or pair[b] != st.pop():
            return False
        # else:
        #     if not st:
        #         return False
        #     elif st[-1] != pair[b]:
        #         return False
        #     st.pop()
    return not st

def isValid_3(self, s: str) -> bool:
    stack = []
    left = ['(', '{', '[']
    if len(s) % 2 == 1:
        return False

    for p in s:
        if p in left:
            stack.append(p)
        else:
            if not stack:
                stack.append(p)
            elif p == ')' and stack[-1] == '(':
                stack.pop()
            elif p == '}' and stack[-1] =='{':
                stack.pop()
            elif p == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    s_1 = "()"
    s_2 = "()[]{}"
    s_3 = "(]"
    print(isValid_2(s_1))
