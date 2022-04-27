from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myStack = []
        result = []
        x = root
        while x or myStack : 
            if x:
                myStack.append(x)
                x = x.left
            else:
                x = myStack.pop()
                result.append(x.val)
                x = x.right
        return  result




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
    [1, 3, 2],
    [4, 2, 5, 1, 6, 3],
    [1, 5, 7, 8, 10, 12]
]

s = Solution()

for root, expected in zip(test_cases, expected_results):
    actual = s.inorderTraversal(root)
    assert actual == expected, f'expected {expected}, got {actual}'
    print(actual)
