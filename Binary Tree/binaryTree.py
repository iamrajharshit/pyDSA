from treeNode import TreeNode

def create():
    data= int(input("\n Enter the data to be inserted or type -1 for no insertion"))
    if data ==-1:
        return None
    
    tree=TreeNode(data)
    print("Enter left child of:" + str(data))
    tree.left=create()
    print("Enter right child of:" + str(data))
    tree.right=create()
    return tree

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(str(tree.info)+"->",end="")
        inorder(tree.right)


def preorder(tree):
    if tree:
        print(str(tree.info)+ "->",end="")
        preorder(tree.left)
        preorder(tree.right)    

def postorder(tree):
    postorder(tree.left)
    postorder(tree.right)
    print(str(tree.info)+"->",end="")
    



if __name__ == "__main__":
    tree=None
    tree=create()
    inorder(tree)
    


    def rev(tree):

        i=1
        j = height(tree)

        #Flag to mark a change in the direction of printing nodes
        flag=0

        while( i<=j):

            #if flag is zero print nodes from rtol
            if (flag==0):
                rightTLeft(tree,j)
                