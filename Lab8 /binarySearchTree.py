"""
ENGR 221  Lab 8: Unbalanced Binary Search Tree
Name: Joe Le
Last updated: Nov 9th 2025

Implements an unbalanced Binary Search Tree (BST) storing (key, value) pairs.
Required methods per Homework 8: isEmpty, getRoot, __searchHelp, lookup,
__findSuccessorHelp, __deleteHelp, __traverseHelp. Public wrappers are already
provided (insert, search, findSuccessor, delete, traverse, __str__).  See HW 8. 
"""


class BinarySearchTree:
    """ TODO: DESCRIBE THE BST CLASS HERE """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ TODO: ISEMPTY DOCSTRING HERE """
        return self.__root is None

    
    def getRoot(self):
        """ TODO: GETROOT DOCSTRING HERE """
        return self.__root


    def search(self, goalKey):
        """ TODO: SEARCH DOCSTRING HERE """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ TODO: __SEARCHHELP DOCSTRING HERE """
        # Base case: empty subtree, key not found
        if node is None:
            return None

        # Recurse to the left or right depending on the key comparison
        if goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        if goalKey > node.key:
            return self.__searchHelp(node.right, goalKey)

        # Keys are equal: found the node
        return node


    def lookup(self, goal):
        """ TODO: LOOKUP DOCSTRING HERE """
        # Use search() to locate the node with the given key
        node = self.search(goal)
        # If not found, raise an exception as indicated by the tests
        if node is None:
            raise Exception("Key not in tree.")
        # Otherwise, return the value stored in that node
        return node.value


    def findSuccessor(self, subtreeRoot):
        """ TODO: FINDSUCCESSOR DOCSTRING HERE """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ TODO: __FINDSUCCESSOR DOCSTRING HERE """
        # Base case: empty subtree has no successor
        if node is None:
            return None

        # The successor is the left-most node in this subtree
        if node.left is None:
            return node
        return self.__findSuccessorHelp(node.left)

    
    def delete(self, deleteKey):
        """ TODO: DELETE DOCSTRING HERE """
        self.__root = self.__deleteHelp(self.__root, deleteKey)

    
    def __deleteHelp(self, node, deleteKey):
        """ TODO: __DELETEHELP DOCSTRING HERE """
        # Base case: empty subtree, nothing to delete
        if node is None:
            return None

        # Recurse to find the node to delete
        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        if deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node

        # Now node.key == deleteKey: this is the node to delete

        # Case 1: no children
        if node.left is None and node.right is None:
            replacement = None
        # Case 2: only right child
        elif node.left is None:
            replacement = node.right
        # Case 3: only left child
        elif node.right is None:
            replacement = node.left
        else:
            # Case 4: two children - use inorder successor from right subtree
            successor = self.__findSuccessorHelp(node.right)
            # Copy successor's key/value into this node
            node.key, node.value = successor.key, successor.value
            # Delete successor node from the right subtree
            node.right = self.__deleteHelp(node.right, successor.key)
            replacement = node

        # If this node is the root of the whole tree, update __root
        if node == self.__root:
            self.__root = replacement

        return replacement


    def traverse(self) -> None:
        """ TODO: TRAVERSE DOCSTRING HERE """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ TODO: __TRAVERSEHELP DOCSTRING HERE """
        # In-order traversal: left subtree, current node, right subtree
        if node is None:
            return
        self.__traverseHelp(node.left)
        print(node)
        self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    pass