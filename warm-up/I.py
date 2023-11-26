stack = []
sequence = input()

pairs = {
    "{": "}",
    "(": ")",
    "[": "]",
}

flag = True
for char in sequence:
    if char in pairs:
        stack += [char]
    else:
        if stack and char == pairs[stack[-1]]:
            del stack[-1]
        else:
            flag = False
            break

print("yes" if (flag and (not stack)) else "no")
