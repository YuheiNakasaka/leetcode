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

def search_node(num, node):
    if node == None:
        return
    if node.value == num:
        left_value = node.left.value if node.left != None else 'None'
        right_value = node.right.value if node.right != None else 'None'
        print('Found: ', node.value, ' left: ', left_value, 'right: ', right_value)
        return node
    if node.value > num:
        if node.left != None:
            return search_node(num, node.left)
        else:
            return
    else:
        if node.right != None:
            return search_node(num, node.right)
        else:
            return

def delete_node(num, node):
    parent_node = None
    current_node = node
    direction = 0
    while current_node.value != num:
        if current_node.value > num:
            left_node = current_node.left
            parent_node = current_node
            current_node = left_node
            direction = -1
        else:
            right_node = current_node.right
            parent_node = current_node
            current_node = right_node
            direction = 1
    # 削除対象節が子を持たない場合
    if current_node.left == None and current_node.right == None:
        if direction == -1:
            parent_node.left = None
        else:
            parent_node.right = None
    # 削除対象節が1つだけ子を持つ場合
    elif current_node.left == None or current_node.right == None:
        if direction == -1:
            if current_node.left != None:
                parent_node.left = current_node.left
            else:
                parent_node.left = current_node.right
        else:
            if current_node.left != None:
                parent_node.right = current_node.left
            else:
                parent_node.right = current_node.right
    else:
        left_biggest = current_node.left
        while left_biggest.right != None:
            left_biggest = left_biggest.right
        if direction == -1:
            left_biggest.left = None if current_node.left.value == left_biggest.value else current_node.left
            left_biggest.right = None if current_node.right.value == left_biggest.value else current_node.right
            parent_node.left = left_biggest
        else:
            left_biggest.left = None if current_node.left.value == left_biggest.value else current_node.left
            left_biggest.right = None if current_node.right.value == left_biggest.value else current_node.right
            parent_node.right = left_biggest


def traverse_tree(node):
    if node.left == None and node.right == None:
        return
    if node.left != None:
        print("parent: ", node.value, " left: ", node.left.value)
        traverse_tree(node.left)
    if node.right != None:
        print("parent: ", node.value, " right: ", node.right.value)
        traverse_tree(node.right)

def create_tree():
    #           47
    #      23       61
    #   17   35    53 72
    # 15 20 31          88
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
    return t

print("== Output ==")
t = create_tree()
traverse_tree(t)
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

print("\n== Output ==")
search_node(23, t)
search_node(20, t)
search_node(72, t)

print("\n== Output ==")
t = create_tree()
delete_node(20, t)
traverse_tree(t)
# == Output ==
# parent:  47  left:  23
# parent:  23  left:  17
# parent:  17  left:  15
# parent:  23  right:  35
# parent:  35  left:  31
# parent:  47  right:  61
# parent:  61  left:  53
# parent:  61  right:  72
# parent:  72  right:  88

print("\n== Output ==")
t = create_tree()
delete_node(72, t)
traverse_tree(t)
# == Output ==
# parent:  47  left:  23
# parent:  23  left:  17
# parent:  17  left:  15
# parent:  17  right:  20
# parent:  23  right:  35
# parent:  35  left:  31
# parent:  47  right:  61
# parent:  61  left:  53
# parent:  61  right:  88

print("\n== Output ==")
t = create_tree()
delete_node(23, t)
traverse_tree(t)
# == Output ==
# parent:  47  left:  20
# parent:  20  left:  17
# parent:  17  left:  15
# parent:  23  right:  35
# parent:  35  left:  31
# parent:  47  right:  61
# parent:  61  left:  53
# parent:  61  right:  72
# parent:  72  right:  88
