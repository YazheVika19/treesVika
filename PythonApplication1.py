from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    def inTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        return self.inTraversal(root.left) + [root.val] + self.inTraversal(root.right)
    def postTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        return self.postTraversal(root.left) + self.postTraversal(root.right) + [root.val]
            

test_cases = [
    None,
    TreeNode(1),
    TreeNode(1, right=TreeNode(2, left=TreeNode(3))),
    TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6))),
    TreeNode(8, left=TreeNode(5, left=TreeNode(1), right=TreeNode(7)), right=TreeNode(10, right=TreeNode(12)))
]

expected_results = [
    [],
    [1],
    [3, 2, 1],
    [4, 5, 2, 6, 3, 1],
    [1, 7, 5, 12, 10, 8]
]

s = Solution()

for root, expected in zip(test_cases, expected_results):
    actual = s.postTraversal(root)
    assert actual == expected, f'expected {expected}, got {actual}'
    print(actual)
