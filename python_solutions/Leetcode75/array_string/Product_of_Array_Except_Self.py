from typing import List

# Time limit exceeded

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         arr = []
#         for i in range(len(nums)):
#             num = nums.pop(0)
#             prod = 1
#             for j in nums:
#                 prod *= j
#             arr.append(prod)
#             nums.append(num)
#
#         return arr
#
#
# print(Solution().productExceptSelf([-1,1,0,-3,3]))


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result