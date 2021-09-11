def maxErasure(self, nums: List[int]) -> int:
        maxUniqueSum = 0
        uniqueSet = set()
        uniqueSum = 0
        i = 0
        for n in nums:
            if n not in uniqueSet:
                uniqueSet.add(n)
                uniqueSum += n
                if uniqueSum > maxUniqueSum:
                    maxUniqueSum = uniqueSum
            else:
                while nums[i] != n:
                    uniqueSet.remove(nums[i])
                    uniqueSum -= nums[i]
                    i += 1
                i += 1
        return maxUniqueSum
