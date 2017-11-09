def multiply(num1, num2):
    product = 0
    num1_size = len(num1)
    num2_size = len(num2)
    for i in range(num1_size-1,-1,-1):
        zeros1 = (num1_size - 1) - i
        value1 = int(num1[i]) * (10**zeros1)
        for j in range(num2_size-1,-1,-1):
            zeros2 = (num2_size - 1) - j
            value2 = int(num2[j]) * (10**zeros2)
            product += (value1 * value2)
    return product