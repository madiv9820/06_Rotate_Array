import warnings
from typing import List

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        # ⚙️ Edge case: If array has only one element, rotation not needed
        if len(nums) == 1: return

        # ✅ Proceed only if k is non-negative
        if k >= 0:
            n: int = len(nums)  # 📏 Step 1: Calculate length of array
            k = k % n   # 🔁 Step 2: Adjust k to handle cases where k > n
            extraMemory: List[int] = [0] * n    # 💾 Step 3: Create a temporary array to hold rotated elements

            # 🚚 Step 4: Compute the new position of each element
            for currentIndex in range(n):
                # 🧮 Calculate where the current element should go
                actualIndex: int = (currentIndex + k) % n
                extraMemory[actualIndex] = nums[currentIndex]

            # 🔄 Step 5: Copy elements back from extraMemory to nums
            for currentIndex in range(n): 
                nums[currentIndex] = extraMemory[currentIndex]

        # ⚠️ Edge case: If k is negative, show a warning
        else:
            warnings.warn('k cannot be negative', category=UserWarning)