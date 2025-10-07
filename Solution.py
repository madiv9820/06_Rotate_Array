import warnings
from typing import List

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        # ⚙️ Step 1: Edge case — single element array doesn’t need rotation
        if len(nums) == 1: return

        # ✅ Step 2: Proceed only if k is non-negative
        if k >= 0:
            n: int = len(nums)
            k = k % n   # 🔁 Step 3: Normalize k to stay within array bounds
            
            if k == 0: return  # 🧱 If k = 0, no rotation needed

            # 🔁 Step 4: Helper function to reverse part of the array
            def reverse(start: int, end: int) -> None:
                """Reverses the portion of nums between start and end indices 🔁"""
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]  # 🔄 Swap elements
                    start, end = start + 1, end - 1
            
            reverse(0, n - 1)   # 🧩 Step 5: Reverse the entire array to get final rotated version
            reverse(0, k - 1)   # 🧩 Step 6: Reverse first part (from 0 to k-1)
            reverse(k, n - 1)   # 🧩 Step 7: Reverse second part (from k to end)
            
        # ⚠️ Step 8: Warn if k is negative
        else:
            warnings.warn('k cannot be negative', category = UserWarning)