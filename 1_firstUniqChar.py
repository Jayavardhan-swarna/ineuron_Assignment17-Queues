def firstUniqChar(s):
    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1  # No non-repeating character found


print(firstUniqChar("leetcode"))     # Output: 0
print(firstUniqChar("loveleetcode")) # Output: 2
print(firstUniqChar("aabb"))         # Output: -1
