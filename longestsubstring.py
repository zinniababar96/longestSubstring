def longest_substring(s):
    char_map={}
    max_length=0
    left=0

    for right in range(len(s)):

        if s[right] in char_map and left<=char_map[s[right]]:
            left=char_map[s[right]]+1
        
        char_map[s[right]]=right
        max_length=max(max_length,right-left+1)
    
    return max_length



s = "abcabcbb"
print(longest_substring(s))