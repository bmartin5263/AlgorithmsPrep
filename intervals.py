def merge(left, right):
    leftPointer = 0
    rightPointer = 0
    result = []

    if left[leftPointer][0] <= right[rightPointer][0]:
        start = left[leftPointer][0]
        end = left[leftPointer][1]
        leftPointer +=1
    else:
        start = right[rightPointer][0]
        end = right[rightPointer][1]
        rightPointer += 1

    while leftPointer < len(left) or rightPointer < len(right):
        print(leftPointer)
        print(rightPointer)
        if leftPointer < len(left) and start <= left[leftPointer][0] and end >= left[leftPointer][0]:
            end = max(end, left[leftPointer][1])
            leftPointer += 1
        elif rightPointer < len(right) and start <= right[rightPointer][0] and end >= right[rightPointer][0]:
            end = max(end, right[rightPointer][1])
            rightPointer += 1
        else:
            result.append((start, end))

            if leftPointer < len(left) and rightPointer < len(right):
                start = min(left[leftPointer][0], right[rightPointer][0])
                end = left[leftPointer][1] if start == left[leftPointer][0] else right[rightPointer][1]
            elif leftPointer < len(left):
                start = left[leftPointer][0]
                end = left[leftPointer][1]
            else:
                start = right[rightPointer][0]
                end = right[rightPointer][1]

    result.append((start, end))

    return result

if __name__ == '__main__':
    left = [(1,3)]
    right = [(5,6)]
    print(merge(left, right))