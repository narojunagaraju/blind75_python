# Tc O(n)
# Sc O(n)

def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char == ')' and (not stack or stack.pop() != '('):
            return False
        elif char == '}' and (not stack or stack.pop() != '{'):
            return False
        elif char == ']' and (not stack or stack.pop() != '['):
            return False
    return not stack

if __name__ == "__main__":
    s = "()"
    print(is_valid(s))
