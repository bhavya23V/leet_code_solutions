class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_value = postorder.pop()
        root = TreeNode(root_value)
        index = inorder.index(root_value)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root