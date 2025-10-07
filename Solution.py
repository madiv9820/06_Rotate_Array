from typing import List
import warnings

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        # ⚙️ Edge case 1: If array has only one element, rotation doesn't matter
        if len(nums) == 1: return
        
        # ⚠️ Edge case 2: If k is negative, raise a warning and exit
        if k < 0: 
            warnings.warn('k cannot be negative', category=UserWarning)
            return
        
        n: int = len(nums)  # 📏 Step 1: Get the length of the array
        k = k % n           # 🔁 Step 2: Handle cases where k > n by taking modulo

        # 🚚 Step 3: Perform rotation k times
        for _ in range(k):        
            lastElement: int = nums[-1]     # 🧩 Store the last element before shifting
            # ⏪ Step 4: Shift all elements one step to the right
            for index in range(n-1, -1, -1): nums[index] = nums[index-1]    
            nums[0] = lastElement   # 🏁 Step 5: Place the last element at the beginning