class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(key)
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(key)
                        break

    def search(self, key):
        current_node = self.root
        while current_node:
            if key == current_node.key:
                return True
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)

    print(bst.search(4))  
    print(bst.search(6))  
