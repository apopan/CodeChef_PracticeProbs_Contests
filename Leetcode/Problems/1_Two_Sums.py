# Solution 1 : Brute force method which results in time complexity of O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target :
                    return [i, j]
                  
          
# Solutoin 2 : Using dictionary to store and compare the values for reducing time complexity to O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       secondaryPair = dict()
       for i in range(len(nums)):
           x = nums[i]
           primaryPair = target - x
          
           if x in secondaryPair:
               return [secondaryPair[x], i]
           else:
                secondaryPair[primaryPair] = i
