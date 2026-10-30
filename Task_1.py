class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_min_iterative(root):
    if root is None:
        return None  # Дерево порожнє
    
    current = root
    while current.left is not None:
        current = current.left
        
    return current.val  # Повертаємо ключ найлівішого вузла

if __name__ == "__main__":
    root = None
    for value in (5, 3, 2, 4, 7, 6, 8):
        root = insert(root, value)

    print(root)
    print(f"Найменше значення: {find_min_iterative(root)}")
