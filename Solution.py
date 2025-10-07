from collections import deque
import warnings
from typing import List, Deque

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0: return  # 🧩 If the array is empty, nothing to rotate

        # ✅ Proceed only if k is non-negative
        if k >= 0: 
            n: int = len(nums)
            q: Deque = deque(nums)

            k = k % n   # ⚙️ Handle rotations greater than array length
            q.rotate(k) # 🔁 Rotate deque by k steps (no keyword argument)

            for index in range(len(q)): nums[index] = q[index]  # 🧱 Copy rotated elements back into original list

        else:
            # ⚠️ Raise a user warning if k is negative
            warnings.warn('k cannot be negative', category = UserWarning)