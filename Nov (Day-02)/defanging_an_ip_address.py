def defang_ip(address):
    result = []
    for ch in address:
        if ch == ".":
            result.append("[.]")
        else:
            result.append(ch)
    return "".join(result)
address = "1.1.1.1"
print(defang_ip(address))
