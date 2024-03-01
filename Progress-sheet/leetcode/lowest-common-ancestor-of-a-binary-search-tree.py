# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        def search (root ,p,q) :
            if root :
                if root.val==p.val:
                    return p
                elif root.val==q.val:
                    return q     
                elif p.val>root.val and q.val>root.val:
                    return search(root.right,p,q)
                elif p.val<root.val and q.val<root.val:
                    return search(root.left,p,q)
                else:
                    return root
        return search (root,p,q)
                
                    
                        