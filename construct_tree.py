__author__ = 'hechaoyi'

'''
[leetcode]Convert Sorted Array to Binary Search Tree @ Python
原题地址：http://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

题意：将一个排序好的数组转换为一颗二叉查找树，这颗二叉查找树要求是平衡的。

解题思路：由于要求二叉查找树是平衡的。所以我们可以选在数组的中间那个数当树根root，然后这个数左边的数组为左子树，右边的数组为右子树，分别递归产生左右子树就可以了。

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(num[0])
        root = TreeNode(num[length / 2])
        root.left = self.sortedArrayToBST(num[:length/2])
        root.right = self.sortedArrayToBST(num[length/2 + 1:])
        return root








'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Analysis:

A not hard question. Use the straight forward idea: get values from that list and save them into a array. Then convert that sorted array into a balanced BST.


Convert Sorted List to Binary Search Tree:

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        cur=head
        if head is None: return None
        sortedlist=[]
        while cur is not None:
            sortedlist.append(cur.val)
            cur=cur.next
        head=self.convertToBST(sortedlist)
        return head

    def convertToBST(self,sortedlist):
        if len(sortedlist)==0: return None
        if len(sortedlist)==1: return TreeNode(sortedlist[0])
        mid=int(len(sortedlist)/2)
        root=TreeNode(sortedlist[mid])
        root.left=self.convertToBST(sortedlist[:mid])
        root.right=self.convertToBST(sortedlist[mid+1:])
        return root



