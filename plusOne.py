def plusOne(digits):
    digits[-1] += 1
    for i in range(len(digits)-1,-1,-1):
        if digits[i] >= 10:
            digits[i] = digits[i] % 10
            if i > 0:
                digits[i-1] += 1
            else:
                digits.insert(0,1)
        else:
            return digits
    return digits

if __name__ == '__main__':
    print(plusOne([9,8,9,9]))