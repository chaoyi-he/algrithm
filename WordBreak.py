#coding:utf-8
__author__ = 'hechaoyi'


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # @good coding!
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for k in range(i):
                tmp =s[k:i]
                if dp[k] and tmp in dict:
                    dp[i] = True
        print(dp)
        return dp[len(s)-1]

if __name__=="__main__":
    s = "leetcode"
    dict = ["leet", "code"]
    print( Solution().wordBreak(s,dict))

    print(len(s))
    print(s[1:9])

#最长公共子串