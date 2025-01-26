# TreeNode class
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.val, end=' ')
            self._inorder_recursive(node.right)

    def depth(self):
        return self._depth_recursive(self.root)

    def _depth_recursive(self, node):
        if node is None:
            return 0
        else:
            left_depth = self._depth_recursive(node.left)
            right_depth = self._depth_recursive(node.right)
            return max(left_depth, right_depth) + 1

    def mirror(self):
        self.root = self._mirror_recursive(self.root)

    def _mirror_recursive(self, node):
        if node is None:
            return None
        left = self._mirror_recursive(node.left)
        right = self._mirror_recursive(node.right)
        node.left, node.right = right, left
        return node

    def copy(self):
        new_tree = BinarySearchTree()
        new_tree.root = self._copy_recursive(self.root)
        return new_tree

    def _copy_recursive(self, node):
        if node is None:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self._copy_recursive(node.left)
        new_node.right = self._copy_recursive(node.right)
        return new_node

    def display_parent_nodes(self):
        self._display_parent_nodes(self.root)

    def _display_parent_nodes(self, node):
        if node is None:
            return
        if node.left or node.right:
            children = []
            if node.left:
                children.append(node.left.val)
            if node.right:
                children.append(node.right.val)
            print(f"Parent: {node.val}, Children: {children}")
        self._display_parent_nodes(node.left)
        self._display_parent_nodes(node.right)

    def display_leaf_nodes(self):
        print("Leaf nodes: ", end='')
        self._display_leaf_nodes(self.root)
        print()

    def _display_leaf_nodes(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.val, end=' ')
            self._display_leaf_nodes(node.left)
            self._display_leaf_nodes(node.right)

    def display_level_order(self):
        if not self.root:
            print("Tree is empty.")
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.val, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

# Main code to demonstrate BinarySearchTree
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [15, 10, 20, 8, 12, 17, 25, 10]
    for elem in elements:
        bst.insert(elem)

    print("In-order Traversal of the BST:")
    bst.inorder()

    search_value = 10
    found_node = bst.search(search_value)
    print(f"Search for {search_value}: {'Found' if found_node else 'Not Found'}")

    delete_value = 10
    bst.delete(delete_value)
    print(f"In-order Traversal after deleting {delete_value}:")
    bst.inorder()

    print(f"Depth of the tree: {bst.depth()}")

    bst.mirror()
    print("In-order Traversal of the mirror image of the BST:")
    bst.inorder()

    copied_tree = bst.copy()
    print("In-order Traversal of the copied BST:")
    copied_tree.inorder()

    print("Parent nodes with their children:")
    bst.display_parent_nodes()

    bst.display_leaf_nodes()

    print("Level order traversal of the tree:")
    bst.display_level_order()
