def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longest = ""
    length = len(s)
    for i in range(length):
        for j in range(length-1,i-1,-1):
            if s[i] == s[j]:
                palindrome = True
                x = i+1
                y = j-1
                while x < y:
                    if s[x] != s[y]:
                        palindrome = False
                        break
                    x += 1
                    y -= 1
                if palindrome:
                    longest = max(longest, s[i:j+1], key=len)
    return longest


if __name__ == '__main__':
    print(longestPalindrome("abcda"))
