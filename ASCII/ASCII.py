# Training: ASCII by Gizmore

code = input("Enter the code:")
decode_str = []

def ascii_to_str(data):
    global decode_str
    ascii_num = ""
    for i in range(0, len(data)):
        if data[i].isdigit():
            ascii_num += data[i]
        else:
            if ascii_num != "":
                decode_str.append(chr(int(ascii_num)))
                ascii_num = ""
    if ascii_num != "":
        decode_str.append(chr(int(ascii_num)))

ascii_to_str(code)

print("".join(decode_str))


