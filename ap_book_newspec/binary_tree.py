class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.root = None
    def insert_node(self, key, node=None):
        # currentノードの設定
        if node is None:
            node = self.root
        
        if self.root is None:
            # ルートノードの場合
            self.root = Node(key)
        else:
            # ルートノード以外の場合
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    print("left ", node.key, key)
                    return
                else:
                    return self.insert_node(key, node = node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    print("right ", node.key, key)
                    return
                else:
                    return self.insert_node(key, node = node.right)

tree = Tree()
tree.insert_node(10)
tree.insert_node(13)
tree.insert_node(14)
tree.insert_node(8)
tree.insert_node(9)
tree.insert_node(7)
tree.insert_node(11)
