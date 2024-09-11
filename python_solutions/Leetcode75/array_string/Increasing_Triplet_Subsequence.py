from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


print(Solution().increasingTriplet([1,2,3,4,5]))
print(Solution().increasingTriplet([5,4,3,2,1]))
print(Solution().increasingTriplet([2,1,5,0,4,6]))




