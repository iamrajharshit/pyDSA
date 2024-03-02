'''  Invert the binary tree!
      *4               4  
     / \              / \
    *2  *7   -->     7  2
   /\  /\           /\  /\   
  1 3 6  9         9 6  3 1 
'''
#post order
#using recursion
#base case is when we find a child with null values
#we go left then right then to the node; and swap left to right

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        


class Solution:
    root=[4,2,7,1,3,6,9]  


    def invertTree(self,root):

        def reverse_node(node):
            if node == None:
                return
            reverse_node(node.left)
            reverse_node(node.right)

            hold= node.left
            node.right=node.right
            node.right=hold


        reverse_node(root)
        return root
    

ans=Solution()
print(ans.root)
print(ans.invertTree)   

