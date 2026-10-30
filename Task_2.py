class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def sum_tree(root):
    """Повертає суму значень усіх вузлів дерева."""
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)


if __name__ == "__main__":
    root = None
    for value in (5, 3, 2, 4, 7, 6, 8):
        root = insert(root, value)

    print(f"Сума всіх значень: {sum_tree(root)}")
 