import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # result = []

        # def dfs(node, depth):
        #     if node is None:
        #         return None
        #     if len(result) == depth:
        #         result.append([])
        #     result[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)

        # dfs(root, 0)
        # return result

        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            temp = []
            for _ in range(len(queue)):
                current = queue.popleft()
                if current:
                    temp.append(current.val)
                    queue.append(current.left)
                    queue.append(current.left)
            if temp:
                result.append(temp)

        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
