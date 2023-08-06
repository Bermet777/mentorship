class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    if root is None:
        return BinaryTreeNode(newValue)
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

def height(root):
    if root is None:
        return 0
    return max(height(root.leftChild), height(root.rightChild)) + 1

def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.leftChild)
    right_height = height(root.rightChild)
    return abs(left_height - right_height) <= 1 and is_balanced(root.leftChild) and is_balanced(root.rightChild)


if __name__ == "__main__":
    root = insert(None, 15)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    
    print("True if binary tree is balanced:")
    print(is_balanced(root))
