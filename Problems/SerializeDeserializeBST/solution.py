# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    NULL_NODE = "null"
    DELIMITER = ","

    def serialize(self, root):

        def serialize_node(node):
        
            if node == None:
                return self.NULL_NODE + self.DELIMITER
            
            left_serialized = serialize_node(node.left)
            
            right_serialized = serialize_node(node.right)
            
            return str(node.val) + self.DELIMITER + left_serialized + right_serialized
    
        return serialize_node(root).rstrip(self.DELIMITER)
        

    def deserialize(self, data):

        nodes = data.split(self.DELIMITER)

        def deserialize_node(nodes):
            
            new_value = nodes.pop()
            
            if new_value == self.NULL_NODE:
                return None
            
            new_node = TreeNode(new_value)
            new_node.left = deserialize_node(nodes)
            new_node.right = deserialize_node(nodes)
            
            return new_node
        
        root = deserialize_node(nodes[::-1])
        
        return root