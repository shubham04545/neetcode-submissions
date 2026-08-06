class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums=set()
        for i in nums:
            if i in snums:
                return True
            snums.add(i)
        return False
       