# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None
        if root == p or root == q:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root and q.val < root:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
        


def build_tree_from_list(lst):
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


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


tree = build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = find_node(tree, 5)
q = find_node(tree, 1)
print(Solution().lowestCommonAncestor(tree, p, q).val)  # Output should be 3

tree = build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = find_node(tree, 5)
q = find_node(tree, 4)
print(Solution().lowestCommonAncestor(tree, p, q).val)  # Output should be 5
