__author__ = 'hechaoyi'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归方式
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

#树的一个例子
class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()

    def add(self, elem):
        """为树加入节点"""
        node = Node(elem)
        if self.root.elem == -1:            #假设树是空的。则对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:                      #对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)


#非递归方式和递归方式 （详细说明：http://www.cnblogs.com/zuoyuan/p/3720273.html）
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    #非递归方式
    def iterative_inorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                list.append(root.val)
                root = root.right
        return list
    #递归方式
    def recursive_inorder(self, root, list):
        if root:
            self.inorder(root.left, list)
            list.append(root.val)
            self.inorder(root.right, list)

    def inorderTraversal(self, root):
        list = []
        self.iterative_inorder(root, list)
        return list



#preorder 递归：

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def iterative_preorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list

    def recursive_preorder(self, root, list):
        if root:
            list.append(root.val)
            self.preorder(root.left,list)
            self.preorder(root.right,list)

    def preorderTraversal(self,root):
        list = []
        self.iterative_preorder(root,list)
        return list

'''
非递归方式等代码： and  http://www.jianshu.com/p/49c8cfd07410  and http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html
/*二叉树的遍历* 2011.8.25*/

#include <iostream>
#include<string.h>
#include<stack>
using namespace std;

typedef struct node
{
    char data;
    struct node *lchild,*rchild;
}BinTree;

typedef struct node1
{
    BinTree *btnode;
    bool isFirst;
}BTNode;


void creatBinTree(char *s,BinTree *&root)  //创建二叉树，s为形如A(B,C(D,E))形式的字符串
{
    int i;
    bool isRight=false;
    stack<BinTree*> s1;          //存放结点
    stack<char> s2;              //存放分隔符
    BinTree *p,*temp;
    root->data=s[0];
    root->lchild=NULL;
    root->rchild=NULL;
    s1.push(root);
    i=1;
    while(i<strlen(s))
    {
        if(s[i]=='(')
        {
            s2.push(s[i]);
            isRight=false;
        }
        else if(s[i]==',')
        {
            isRight=true;
        }
        else if(s[i]==')')
        {
            s1.pop();
            s2.pop();
        }
        else if(isalpha(s[i]))
        {
            p=(BinTree *)malloc(sizeof(BinTree));
            p->data=s[i];
            p->lchild=NULL;
            p->rchild=NULL;
            temp=s1.top();
            if(isRight==true)
            {
                temp->rchild=p;
                cout<<temp->data<<"的右孩子是"<<s[i]<<endl;
            }
            else
            {
                temp->lchild=p;
                cout<<temp->data<<"的左孩子是"<<s[i]<<endl;
            }
            if(s[i+1]=='(')
                s1.push(p);
        }
        i++;
    }
}

void display(BinTree *root)        //显示树形结构
{
    if(root!=NULL)
    {
        cout<<root->data;
        if(root->lchild!=NULL)
        {
            cout<<'(';
            display(root->lchild);
        }
        if(root->rchild!=NULL)
        {
            cout<<',';
            display(root->rchild);
            cout<<')';
        }
    }
}

void preOrder1(BinTree *root)     //递归前序遍历
{
    if(root!=NULL)
    {
        cout<<root->data<<" ";
        preOrder1(root->lchild);
        preOrder1(root->rchild);
    }
}

void inOrder1(BinTree *root)      //递归中序遍历
{
    if(root!=NULL)
    {
        inOrder1(root->lchild);
        cout<<root->data<<" ";
        inOrder1(root->rchild);
    }
}

void postOrder1(BinTree *root)    //递归后序遍历
{
    if(root!=NULL)
    {
        postOrder1(root->lchild);
        postOrder1(root->rchild);
        cout<<root->data<<" ";
    }
}

void preOrder2(BinTree *root)     //非递归前序遍历
{
    stack<BinTree*> s;
    BinTree *p=root;
    while(p!=NULL||!s.empty())
    {
        while(p!=NULL)
        {
            cout<<p->data<<" ";
            s.push(p);
            p=p->lchild;
        }
        if(!s.empty())
        {
            p=s.top();
            s.pop();
            p=p->rchild;
        }
    }
}

void inOrder2(BinTree *root)      //非递归中序遍历
{
    stack<BinTree*> s;
    BinTree *p=root;
    while(p!=NULL||!s.empty())
    {
        while(p!=NULL)
        {
            s.push(p);
            p=p->lchild;
        }
        if(!s.empty())
        {
            p=s.top();
            cout<<p->data<<" ";
            s.pop();
            p=p->rchild;
        }
    }
}

void postOrder2(BinTree *root)    //非递归后序遍历
{
    stack<BTNode*> s;
    BinTree *p=root;
    BTNode *temp;
    while(p!=NULL||!s.empty())
    {
        while(p!=NULL)              //沿左子树一直往下搜索，直至出现没有左子树的结点
         {
            BTNode *btn=(BTNode *)malloc(sizeof(BTNode));
            btn->btnode=p;
            btn->isFirst=true;
            s.push(btn);
            p=p->lchild;
        }
        if(!s.empty())
        {
            temp=s.top();
            s.pop();
            if(temp->isFirst==true)     //表示是第一次出现在栈顶
             {
                temp->isFirst=false;
                s.push(temp);
                p=temp->btnode->rchild;
            }
            else                        //第二次出现在栈顶
             {
                cout<<temp->btnode->data<<" ";
                p=NULL;
            }
        }
    }
}

void postOrder3(BinTree *root)     //非递归后序遍历
{
    stack<BinTree*> s;
    BinTree *cur;                      //当前结点
    BinTree *pre=NULL;                 //前一次访问的结点
    s.push(root);
    while(!s.empty())
    {
        cur=s.top();
        if((cur->lchild==NULL&&cur->rchild==NULL)||
           (pre!=NULL&&(pre==cur->lchild||pre==cur->rchild)))
        {
            cout<<cur->data<<" ";  //如果当前结点没有孩子结点或者孩子节点都已被访问过
              s.pop();
            pre=cur;
        }
        else
        {
            if(cur->rchild!=NULL)
                s.push(cur->rchild);
            if(cur->lchild!=NULL)
                s.push(cur->lchild);
        }
    }
}


int main(int argc, char *argv[])
{
    char s[100];
    while(scanf("%s",s)==1)
    {
        BinTree *root=(BinTree *)malloc(sizeof(BinTree));
        creatBinTree(s,root);
        display(root);
        cout<<endl;
        preOrder2(root);
        cout<<endl;
        inOrder2(root);
        cout<<endl;
        postOrder2(root);
        cout<<endl;
        postOrder3(root);
        cout<<endl;
    }
    return 0;
}

'''