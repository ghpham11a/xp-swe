# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root, key):
        # Base case: if the root is None, just return None
        if not root:
            return root

        # If the key to be deleted is greater than the root's value,
        # it lies in the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If the key to be deleted is less than the root's value,
        # it lies in the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the current node matches the key, this is the node to delete
        else:
            # Case 1: Node has no left child, so we replace it with its right child
            if not root.left:
                return root.right

            # Case 2: Node has no right child, so we replace it with its left child
            elif not root.right:
                return root.left

            # Case 3: Node has two children
            # We find the smallest node in the right subtree (in-order successor)
            cur = root.right
            while cur.left:
                cur = cur.left

            # Replace current node's value with that successor value
            root.val = cur.val

            # Recursively delete the in-order successor from right subtree
            root.right = self.deleteNode(root.right, root.val)

        # Return the (possibly updated) root
        return root