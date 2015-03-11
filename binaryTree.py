class BinaryNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)

    def delete(self, value):
        if self.left == self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        """ balancing """
        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = child.value
        else:
            self.left = child.left
            self.value = child.value

        return self


class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            elif target < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, value):
        if self.root:
            self.root = self.removeFromParent(self.root, value)

    def removeFromParent(self, parent, value):
        if parent is None:
            return None

        if value == parent.value:
            return parent.delete(value)
        elif value < parent.value:
            parent.left = self.removeFromParent(parent.left, value)
        else:
            parent.right = self.removeFromParent(parent.right, value)

        return parent


import random
from time import time


def performance():
    n = 1024
    while n < 65536:
        bt = BinaryTree()
        for i in range(n):
            bt.add(random.randint(1, n))

        now = time()
        bt.contains(random.randint(1, n))
        print(n, (time() - now) * 1000)

        n *= 2
