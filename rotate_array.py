#coding:utf-8
__author__ = 'hechaoyi'


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]

class Solution1:
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    #交换获得方式
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        print("1",nums)
        self.reverse(nums, 0, k)
        print("2",nums)
        self.reverse(nums, k, len(nums))
        print("3",nums)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

    #直接拼接形式
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(nums[len(nums) - k:])
        print(nums[:len(nums) - k])
        print(nums[1:3]) #不包括最后面的那个索引

        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution1().rotate2(nums, 3)
    print nums