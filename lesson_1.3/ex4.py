def is_brackets_closed(text, brackets="()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = [] 
    for character in text:
        if character in opening: 
            stack.append(opening.index(character))
        elif character in closing: 
            if stack and stack[-1] == closing.index(character):
                stack.pop()  
            else:
                return False 

    return (not stack)

print(is_brackets_closed("[{}({})]"))
print(is_brackets_closed("{]"))
print(is_brackets_closed("{"))