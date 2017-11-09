def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums1.extend(nums2)
    merged = sorted(nums1)
    mergedLen = len(merged)
    if mergedLen == 0:
        return float(0)
    isEven = mergedLen % 2 == 0
    middle = (mergedLen//2) - 1
    if isEven:
        return (merged[middle] + merged[middle+1]) / 2
    else:
        return float(merged[middle+1])

if __name__ == '__main__':
    # 1 2 3 4 5 6 7 8
    print(findMedianSortedArrays([],[]))