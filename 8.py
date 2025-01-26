# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

# ExpressionTree class
class ExpressionTree:
    def construct_from_postfix(self, postfix):
        stack = []
        for char in postfix:
            node = Node(char)
            if char in "+-*/":
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack.pop()

    # Recursive Traversals
    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.value, end=' ')
            self.inorder_recursive(node.right)

    def preorder_recursive(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_recursive(node.left)
            self.preorder_recursive(node.right)

    def postorder_recursive(self, node):
        if node:
            self.postorder_recursive(node.left)
            self.postorder_recursive(node.right)
            print(node.value, end=' ')

    # Non-Recursive Traversals
    def inorder_non_recursive(self):
        stack, node = [], self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.value, end=' ')
            node = node.right

    def preorder_non_recursive(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder_non_recursive(self):
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().value, end=' ')

# Example usage
if __name__ == "__main__":
    exp_tree = ExpressionTree()
    postfix = "ab+ef*g*-"
    exp_tree.construct_from_postfix(postfix)

    print("In-order (Recursive):", end=" ")
    exp_tree.inorder_recursive(exp_tree.root)

    print("\nPre-order (Recursive):", end=" ")
    exp_tree.preorder_recursive(exp_tree.root)

    print("\nPost-order (Recursive):", end=" ")
    exp_tree.postorder_recursive(exp_tree.root)

    print("\nIn-order (Non-Recursive):", end=" ")
    exp_tree.inorder_non_recursive()

    print("\nPre-order (Non-Recursive):", end=" ")
    exp_tree.preorder_non_recursive()

    print("\nPost-order (Non-Recursive):", end=" ")
    exp_tree.postorder_non_recursive()
