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
        # Recursive search for goalKey starting at node
        if node is None:
            return None
        if goalKey == node.key:
            return node
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        else:
            return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        """ TODO: LOOKUP DOCSTRING HERE """
        # Return value for key == goal, or raise if absent
        found = self.search(goal)
        if found is None:
            raise Exception("Key not in tree.")
        return found.value

    def findSuccessor(self, subtreeRoot):
        """ TODO: FINDSUCCESSOR DOCSTRING HERE """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ TODO: __FINDSUCCESSOR DOCSTRING HERE """
         # Return the left-most (minimum) node in this subtree
        if node is None:
            return None
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def delete(self, deleteKey):
        """ TODO: DELETE DOCSTRING HERE """
        self.__root = self.__deleteHelp(self.__root, deleteKey)

    
    def __deleteHelp(self, node, deleteKey):
        """ TODO: __DELETEHELP DOCSTRING HERE """
        # Recursive delete. Return new subtree root.
       
        """
        Recursive helper for delete(). Returns the (possibly new) root of this subtree.
        Cases:
         • deleteKey < node.key  -> delete in left subtree
         • deleteKey > node.key  -> delete in right subtree
         • equal (found node):
          - 0 children -> return None
          - 1 child    -> return that child
          - 2 children -> replace with inorder successor (min of right subtree)
        """
        if node is None:
            return None

        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        if deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node

        # Found the node to delete
        # Case 0: no children
        if node.left is None and node.right is None:
            return None

        # Case 1a: only right child
        if node.left is None:
            return node.right

        # Case 1b: only left child
        if node.right is None:
            return node.left

        # Case 2: two children — use inorder successor (min of right subtree)
        succ = self.__findSuccessorHelp(node.right)
        node.key, node.value = succ.key, succ.value
        node.right = self.__deleteHelp(node.right, succ.key)
        return node


    def traverse(self) -> None:
        """ TODO: TRAVERSE DOCSTRING HERE """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ TODO: __TRAVERSEHELP DOCSTRING HERE """
        # In-order traversal: left, node, right; prints "key:value"
        if node is None:
            return
        self.__traverseHelp(node.left)
        print(f"({node.key}, {node.value})")
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