def fukkkk(code, inp=""):
    mem, ptr, ip, op, loop = [0] * 30000, 0, 0, "", {}
    
    for i, c in enumerate(code):
        if c == "[": loop[i] = code.find("]", i)
        if c == "]": loop[i] = code.rfind("[", 0, i)

    i, inp_ptr = 0, 0
    while i < len(code):
        c = code[i]
        if c == ">": ptr += 1
        elif c == "<": ptr -= 1
        elif c == "+": mem[ptr] = (mem[ptr] + 1) % 256
        elif c == "-": mem[ptr] = (mem[ptr] - 1) % 256
        elif c == ".": op += chr(mem[ptr])
        elif c == ",": mem[ptr] = ord(inp[inp_ptr]) if inp_ptr < len(inp) else 0; inp_ptr += 1
        elif c == "[" and mem[ptr] == 0: i = loop[i]
        elif c == "]" and mem[ptr] != 0: i = loop[i]
        i += 1

    return op

print(fukkkk("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<+++."))
