#coding:utf-8
__author__ = 'hechaoyi'

'''
原题地址：https://oj.leetcode.com/problems/climbing-stairs/

题意：

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

解题思路：

爬楼梯问题。经典的动态规划问题。每次上一个台阶或者两个台阶，问一共有多少种方法到楼顶。这个实际上就是斐波那契数列的求解。可以逆向来分析问题，如果有n个台阶，那么走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。所以f(n) = f(n-1) + f(n-2)。

'''



class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [1 for i in range(n)] #目的是为了将第一个和第二个的值给出，后面的1对计算没意义
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

if __name__ == "__main__":
    print(Solution().climbStairs(10))
    # print([1 for i in range(3)])