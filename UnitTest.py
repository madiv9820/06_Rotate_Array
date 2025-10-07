import unittest
from timeout_decorator import timeout
from Solution import Solution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
            ([-1,-100,3,99], 2, [3,99,-1,-100]),
            ([1,2,3,4,5], 5, [1,2,3,4,5]),
            ([10,20,30,40,50], 7, [40,50,10,20,30]),
            ([1,2], 3, [2,1]),
            ([99], 10, [99])
            ([1,2,3,4,5,6,7], -100, [1,2,3,4,5,6,7])
        )
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_0(self):
        nums, k, expectedResult = self.__testcases[0]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))
    
    @timeout(0.5)
    def test_case_1(self):
        nums, k, expectedResult = self.__testcases[1]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

    @timeout(0.5)
    def test_case_2(self):
        nums, k, expectedResult = self.__testcases[2]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

    @timeout(0.5)
    def test_case_3(self):
        nums, k, expectedResult = self.__testcases[3]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

    @timeout(0.5)
    def test_case_4(self):
        nums, k, expectedResult = self.__testcases[4]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

    @timeout(0.5)
    def test_case_5(self):
        nums, k, expectedResult = self.__testcases[5]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

    @timeout(0.5)
    def test_case_6(self):
        nums, k, expectedResult = self.__testcases[6]
        self.__solution.rotate(nums = nums, k = k)
        self.assertEqual(all(a == b for a, b in zip(nums, expectedResult)))

if __name__ == '__main__': unittest.main()