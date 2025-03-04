# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []
        while queue:
            qLength = len(queue)
            rightMost = None
            for i in range(qLength):
                node = queue.popleft()
                rightMost = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if rightMost is not None:
                result.append(rightMost)
        return result

    def build_tree_from_list(self, list):
        if not list:
            return None
        root = TreeNode(list[0])
        queue = [root]
        i = 1
        while queue and i < len(list):
            node = queue.pop(0)
            if list[i] is not None:
                node.left = TreeNode(list[i])
                queue.append(node.left)
            i += 1
            if i < len(list) and list[i] is not None:
                node.right = TreeNode(list[i])
                queue.append(node.right)
            i += 1
        return root


print(
    Solution().rightSideView(
        Solution().build_tree_from_list([1, 2, 3, None, 5, None, 4])
    )
)  # [1, 3, 4]
