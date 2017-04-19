__author__ = 'hechaoyi'


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if(root!=None):
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        else:
            return result


