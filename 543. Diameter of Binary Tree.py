# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0

        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            self.maximum = max(self.maximum, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return self.maximum

    def build_tree_from_list(self, lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            node = queue.pop(0)
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root


print(Solution().diameterOfBinaryTree(Solution().build_tree_from_list([1, 2, 3, 4, 5])))
print(Solution().diameterOfBinaryTree(Solution().build_tree_from_list([1, 2])))
print(Solution().diameterOfBinaryTree(Solution().build_tree_from_list([1])))
