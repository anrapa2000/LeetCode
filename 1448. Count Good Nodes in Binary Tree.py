# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0

        def dfs(node, maxValue):
            if node is None:
                return
            if node.val >= maxValue:
                self.count += 1
                maxValue = max(maxValue, node.val)
            dfs(node.left, maxValue)
            dfs(node.right, maxValue)

        dfs(root, root.val)
        return self.count

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
    Solution().goodNodes(Solution().build_tree_from_list([3, 1, 4, 3, None, 1, 5]))
)  # 4
print(Solution().goodNodes(Solution().build_tree_from_list([3, 3, None, 4, 2])))  # 3
print(Solution().goodNodes(Solution().build_tree_from_list([1])))  # 1
print(Solution().goodNodes(Solution().build_tree_from_list([9, None, 3, 6])))  # 1
print(
    Solution().goodNodes(
        Solution().build_tree_from_list([2, None, 4, 10, 8, None, None, 4])
    )
)  # 4
