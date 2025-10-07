# [Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

#### ***Topics: Array, Math, Two Pointers***

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Examples
- **Example 1:** <br> **Input:** $nums = [1,2,3,4,5,6,7]$, $k = 3$ <br> **Output:** $[5,6,7,1,2,3,4]$ <br> **Explanation:** <br> - rotate $1$ steps to the right: $[7,1,2,3,4,5,6]$ <br> - rotate $2$ steps to the right: $[6,7,1,2,3,4,5]$ <br> - rotate $3$ steps to the right: $[5,6,7,1,2,3,4]$

- **Example 2:** <br> **Input:** $nums = [-1,-100,3,99], k = 2$ <br> **Output:** $[3,99,-1,-100]$ <br> **Explanation:** <br> - rotate $1$ steps to the right: $[99,-1,-100,3]$ <br> - rotate $2$ steps to the right: $[3,99,-1,-100]$

### Constraints:
- $\small 1 <= nums.length <= 10^5$
- $\small 2^{31} <= nums[i] <= 2^{31} - 1$
- $\small 0 <= k <= 10^5$

### Follow up:
- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with $\small O(1)$ extra space?