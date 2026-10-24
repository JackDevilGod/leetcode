class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing: bool = False
        decreasing: bool = False

        max_increase: int = 0
        max_decrease: int = 0

        n_increase: int = 0
        n_decrease: int = 0

        previos: int = nums.pop()
        while nums:
            current: int = nums.pop()

            increasing = current > previos
            decreasing = current < previos

            if increasing:
                n_increase += 1
            else:
                max_increase = max(max_increase, n_increase + 1)
                n_increase = 0

            if decreasing:
                n_decrease += 1
            else:
                max_decrease = max(max_decrease, n_decrease + 1)
                n_decrease = 0

            previos = current

        
        max_decrease = max(max_decrease, n_decrease + 1)
        max_increase = max(max_increase, n_increase + 1)

        return max(max_decrease, max_increase)