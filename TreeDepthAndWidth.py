__author__ = 'hechaoyi'

import queue

class Node:
	def __init__(self,value=None,left=None,right=None):
		self.value=value
		self.left=left
		self.right=right

'''递归的思路就是先看一个完整实例的过程（中间调用递归），然后再将最末端的代入看其需要完成什么'''
def treeDepth(tree):
	if tree==None:
		return 0
	leftDepth=treeDepth(tree.left)
	rightDepth=treeDepth(tree.right)
	if leftDepth>rightDepth:
		return leftDepth+1
	if rightDepth>=leftDepth:
		return rightDepth+1

def treeWidth(tree):
	curwidth=1
	maxwidth=0
	q=queue.Queue()
	q.put(tree)
	while not q.empty():
		n=curwidth
		for i in range(n):
			tmp=q.get()
			curwidth-=1 # 减去当前节点对应的那一个个数，因为要去统计他的子节点的个数
			if tmp.left:
				q.put(tmp.left)
				curwidth+=1
			if tmp.right:
				q.put(tmp.right)
				curwidth+=1
		if curwidth>maxwidth:
			maxwidth=curwidth
	return maxwidth

if __name__=='__main__':
	root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
	depth=treeDepth(root)
	width=treeWidth(root)
	print('depth:',depth)
	print('width:',width)