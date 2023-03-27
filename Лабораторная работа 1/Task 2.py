def check_brackets(brackets_row: str) -> bool:
    stack = []
    for bracket in brackets_row:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return len(stack) == 0
