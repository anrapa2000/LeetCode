import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # if root is None:
        #     return None
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left = right
        # root.right = left
        # return root
        
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

    def listToTreeNode(self, arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        i = 1
        queue = [root]
        while i < len(arr):
            current = queue.pop(0)
            if arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1
        return root

    def treeNodeToList(self, node):
        if node is None:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result


value = Solution()
root = value.listToTreeNode([4, 2, 7, 1, 3, 6, 9])
inverted_root = value.invertTree(root)
print(value.treeNodeToList(inverted_root))  # Output should be the inverted tree
