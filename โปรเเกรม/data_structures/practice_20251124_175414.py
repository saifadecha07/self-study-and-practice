# Session: Lunch break learning
# Note: Finally understood this concept!

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