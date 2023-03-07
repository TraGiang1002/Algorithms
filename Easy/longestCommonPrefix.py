from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))