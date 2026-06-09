# Session: Reviewing docs before bed
# Note: Need to memorize this syntax.

# Source: LeetCode Practice Notes
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create root
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(15)