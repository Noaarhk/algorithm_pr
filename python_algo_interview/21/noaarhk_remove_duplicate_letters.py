import collections


def removeDuplicateLetters(s: str) -> str:
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


def solution(s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # while stack -> stack에 글자가 있고, char<stack[-1] 이전에 스택에 쌓인 글자가 현재 글자보다 사전적으로 뒤의 글자이며, counter[stack[-1]]>0
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


if __name__ == '__main__':
    s = "cbacdcbc"
    print(solution(s))
