def firstUniqChar(s):
    # Create a hashmap to store character frequencies
    freq = {}

    # Count the frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first unique character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1
s1 = "leetcode"
print(firstUniqChar(s1))

s2 = "loveleetcode"
print(firstUniqChar(s2))


s3 = "aabb"
print(firstUniqChar(s3))
