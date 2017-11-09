def addBinary(a, b):
    sum = int(a, base=2) + int(b, base=2)
    return bin(sum)[2:]

if __name__ == "__main__":
    print(addBinary("100","101"))