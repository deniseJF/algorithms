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
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False


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
