__author__ = 'hechaoyi'


class tree_node(object):
    def __init__(self,v):
        self.value=v
        self.left= None
        self.right = None

def construct_tree(root,edges):
    if root ==None:
        return None
    for i in range(len(edges)):
        if edges[i][0] == root.value:
            if root.left ==None:
                root.left = tree_node(edges[i][1])
            elif root.right ==None:
                root.right = tree_node(edges[i][1])
    construct_tree(root.left,edges)
    construct_tree(root.right,edges)


def find_ancestor(root,value,ance_list):
    if root.left!=None and root.left.value == value:
        ance_list.append(root.value)
    elif root.right!=None and root.right.value == value:
        ance_list.append(root.value)
    elif root.left!=None and root.right!=None:
        find_ancestor(root.left,value,ance_list)
        find_ancestor(root.right,value,ance_list)
    elif root.left!=None and root.right==None:
        find_ancestor(root.left,value,ance_list)
    elif root.right!=None and root.left==None:
        find_ancestor(root.right,value,ance_list)


def assigned_tree(root,value):
    if root!=None and root.value==value:
        return root
    elif root.left!=None and root.right!=None :
        retl = assigned_tree(root.left,value)
        retr = assigned_tree(root.right,value)
        if retl!=None:
            return retl
        if retr!=None:
            return retr

    elif root.left!=None and root.right==None :
        retl = assigned_tree(root.left,value)
        if retl!=None:
            return retl
    elif root.right!=None and root.left==None :
        retr = assigned_tree(root.right,value)
        if retr!=None:
            return  retr


def tree_size(root,list_vertex):
    if root!=None:
        list_vertex.append(root.value)
        if root.left !=None and root.right!=None :
            tree_size(root.left,list_vertex)
            tree_size(root.right,list_vertex)
        elif root.left!=None and root.right==None :
            tree_size(root.left,list_vertex)
        elif root.right!=None and root.left==None :
            tree_size(root.right,list_vertex)




if __name__=='__main__':
    edges = []
    list1 =[13,12,8,13]
    edge_list = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 7, 12, 5, 9, 5, 8, 6, 11, 6, 10, 11, 13]

    root = tree_node(1)

    for i in range(len(edge_list)):
        if i%2==0 :
            edges.append([edge_list[i],edge_list[i+1]])

    construct_tree(root,edges)


    ance_former_list=[]
    ance_later_list=[]

    find_ancestor(root,list1[2],ance_former_list)
    find_ancestor(root,list1[3],ance_later_list)

    while ance_former_list[len(ance_former_list)-1]!=1:
        find_ancestor(root,ance_former_list[len(ance_former_list)-1],ance_former_list)

    while ance_later_list[len(ance_later_list)-1]!=1:
        find_ancestor(root,ance_later_list[len(ance_later_list)-1],ance_later_list)

    print(edges)
    print(ance_former_list)
    print(ance_later_list)

    if (len(ance_former_list)-len(ance_later_list)>=0):
        min_len = len(ance_later_list)
    else :
        min_len = len(ance_former_list)

    least_common_ancestor = 0
    for i in range(min_len):
        for j in range(min_len):
            if ance_former_list[i]==ance_later_list[j]:
                least_common_ancestor = ance_later_list[j]


    print(least_common_ancestor)

    required_tree = assigned_tree(root,least_common_ancestor)

    list_vertex = []
    tree_size(required_tree,list_vertex)
    print(len(list_vertex))