def balanced_paranthesis(exp):
    stack = []

    for char in exp:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char!= "]":
                    return False

    if stack:
        return False
    return True


if __name__ == "__main__":
    expr = "{()}[]"
    if balanced_paranthesis(expr):
        print("Balanced")
    else:
        print("Not Balanced")
