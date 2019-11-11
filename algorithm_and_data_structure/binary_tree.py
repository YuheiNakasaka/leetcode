# プログラミングの宝箱 アルゴリズムとデータ構造 第2版
# https://amzn.to/2p3hS3w
# P168~
class TreeNode:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None

def insert_tree(num, node):
    if node == None:
        return
    if node.value > num:
        if node.left != None:
            insert_tree(num, node.left)
        else:
            node.left = TreeNode(num)
    else:
        if node.right != None:
            insert_tree(num, node.right)
        else:
            node.right = TreeNode(num)

def search_tree(num, node):
    if node == None:
        return
    if node.value == num:
        left_value = node.left.value if node.left != None else 'None'
        right_value = node.right.value if node.right != None else 'None'
        print('Found: ', node.value, ' left: ', left_value, 'right: ', right_value)
        return node
    if node.value > num:
        if node.left != None:
            return search_tree(num, node.left)
        else:
            return
    else:
        if node.right != None:
            return search_tree(num, node.right)
        else:
            return

def traverse_tree(node):
    if node.left == None and node.right == None:
        return
    if node.left != None:
        print("parent: ", node.value, " left: ", node.left.value)
        traverse_tree(node.left)
    if node.right != None:
        print("parent: ", node.value, " right: ", node.right.value)
        traverse_tree(node.right)


t = TreeNode(47)
insert_tree(23, t)
insert_tree(17, t)
insert_tree(15, t)
insert_tree(20, t)
insert_tree(35, t)
insert_tree(31, t)
insert_tree(61, t)
insert_tree(53, t)
insert_tree(72, t)
insert_tree(88, t)

traverse_tree(t)

search_tree(23, t)
search_tree(20, t)
search_tree(72, t)


# == Output ==
# parent:  47  left:  23
# parent:  23  left:  17
# parent:  17  left:  15
# parent:  17  right:  20
# parent:  23  right:  35
# parent:  35  left:  31
# parent:  47  right:  61
# parent:  61  left:  53
# parent:  61  right:  72
# parent:  72  right:  88