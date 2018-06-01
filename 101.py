class Solution:
    def isSymmetric(self, root):
        return Solution.traverse(root.left, root.right)

    def traverse(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        #left's left child compare with right's right child, left's right child compares with right's left child
        return self(left.left, right.right) and self(left.right, right.left)
