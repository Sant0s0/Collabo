def decimal(x) -> int:
    x = str(x)[::-1]
    result = 0
    for i in range(len(x)):
        if x[i] == "1":
            result += 2**i

    return result

def convert(x) -> str:
    return "0" + bin(x)[2::]