import warnings
from typing import List

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 1: return   # ⚙️ Edge case: If there's only one element, no rotation needed
        
        # ✅ Proceed only if k is positive
        if k > 0:
            # 📏 Step 1: Initialize variables
            cycleCount: int = 0       # 🔢 Keeps track of how many elements have been moved
            n: int = len(nums)
            startIndex: int = 0       # 🏁 Start of the current cycle
            k = k % n                 # 🔁 Adjust k to stay within array bounds

            # 🚴 Step 2: Keep running cycles until all elements are rotated
            while cycleCount < n:
                currentIndex = startIndex          # 📍 Current index position
                prevElement = nums[startIndex]     # 💾 Temporarily store the element to move

                # 🧭 Step 3: Move elements along the cycle until we reach the start again
                while True:
                    nextIndex = (currentIndex + k) % n  # 🔢 Compute new index position
                    # 🔄 Swap the values — move prevElement to nextIndex, 
                    # and store what was there as the new prevElement
                    nums[nextIndex], prevElement = prevElement, nums[nextIndex]

                    # Update tracking values
                    currentIndex, cycleCount = nextIndex, cycleCount + 1

                    # 🛑 Step 4: If we have completed a cycle, break
                    if currentIndex == startIndex: break
                
                # ⏭️ Step 5: Move to the next starting index if any elements remain
                startIndex += 1
        
        # ⚠️ Step 6: Warn if k is negative
        else:
            warnings.warn('k cannot be negative', category = UserWarning)