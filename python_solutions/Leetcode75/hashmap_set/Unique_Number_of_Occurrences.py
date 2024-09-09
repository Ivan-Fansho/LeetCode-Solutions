from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new_dict = {}
        for num in arr:
            if num in new_dict:
                new_dict[num] +=1
            else:
                new_dict[num] = 1
        
        has_duplicates = len(new_dict.values()) == len(set(new_dict.values()))
        
        return has_duplicates
    

arr = [-3,0,1,-3,1,1,1,-3,10,0]

print(Solution().uniqueOccurrences(arr=arr))