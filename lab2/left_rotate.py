from typing import Optional


class Node:
    """
    Class representing a single node of a binary tree containing integer values. 

    ...

    Attributes
    ----------

    value: int
        Value stored in the node.
    parent: Node, optional
        Parent of the current node. Can be None.
    left: Node, optional
        Left child of the current node. Can be None.
    right: Node, optional
        Right child of the current node. Can be None.
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.parent = self.right = self.left = None
    
    def set_left_child(self, node: Optional['Node']) -> None:
        """
        Set the the left child of self to the given node.
        Sets the node's parent to self (if it is not None).

        Args:
            node (Node, optional): the node to set as the child.
        """
        self.left = node
        if node is not None:
            node.parent = self
         
    def set_right_child(self, node: Optional['Node']) -> None:
        """
        Set the the right child of self to the given node.
        Sets the node's parent to self (if it is not None).

        Args:
            node (Node, optional): the node to set as the child.
        """
        self.right = node
        if node is not None:
            node.parent = self

def left_rotation(node: Node, root: Node) -> Node:
    """Left rotate a node

    Do a left rotation on the node specified as the first argument and return the root 
    of the tree. The root can be the specified, second arugment (root) or a new root which
    changed because of the rotation.
    
    Args:
        node (Node): The node on which the rotation is done.
        root (Node): Root node of the binary tree which contains the node which we are rotating.
    
    Returns:
        Node: The root of the binary tree, which could have changed due to the rotation.
    """
    p = node.parent
    x = node
    y = node.right

    if y is None:
        return root

    x.set_right_child(y.left)
    
    if p is None:
        root = y
    elif p.left == x:
        p.set_left_child(y)
    else:
        p.set_right_child(y)
    
    y.set_left_child(x)
    
    return root    
         
def print_tree(node: Optional[Node], level: int = 0) -> None:
    """
    Prints a rough sketch of the tree in the command line.

    Accepts a node which can be None and prints its right subtree, than its value and then its left subtree, recursivevly.
    
    Args:
        node (Node, optional): The node for which we are writing out the subtree.
        level (int): Number of empty lines before the actual value - used to discern the tree levels.
    """
    if node is None:
        return
    print_tree(node.right, level + 2)
    print(' ' * level + f'-> {node.value}')
    print_tree(node.left, level + 2)

root = Node(3)
root.set_left_child(Node(2))
root.left.set_left_child(Node(1))
root.set_right_child(Node(4))
root.right.set_right_child(Node(5))

print('Prije rotacije:')
print_tree(root)

root = left_rotation(root.left, root)

print()
print('Nakon rotacije:')
print_tree(root)
