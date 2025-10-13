"""
Joe Le
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from double_node import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__first_node = None
        self.__last_node = None 

    def is_empty(self):
        return self.__first_node is None

    def first(self):
        return None if self.__first_node is None else self.__first_node.get_value()
    
    
    def get_first_node(self):
        return self.__first_node

    def get_last_node(self):
        return self.__last_node
    
    def set_first_node(self, node):
        if type(node) != DoubleNode and node is not None:
            raise Exception ("Error: Input must be valid DoubleNode or None")
        self.__first_node = node
        if node is None:
            self.__last_node = None

    def set_last_node(self, node):
        if type(node) != DoubleNode and node is not None:
            raise Exception ( " Error: Input must be a valid DoubleNode or None")
        self.__last_node = node
        if node is None: 
            self.__first_node = None

    def find(self, value):
        cur = self.__first_node
        while cur is not None:
            if cur.get_value() == value:
                return cur
            cur = cur.get_next_node()
            return None

    def insert_front(self, value):
        new_node = DoubleNode(value, next=self.__first_node, previous = None)
        if self.__first_node is not None:
            self.__first_node.set_previous_node(new_node)
        else:
            self.__last_node = new_node
        self.__first_node = new_node

    def insert_back(self, value):
        new_node = DoubleNode(value, next = None, previous=self.__last_node)
        if self.__last_node is not None:
            self.__last_node.set_next_node(new_node)
        else:
            self.__first_node = new_node
        self.__last_node = new_node

    def insert_after(self, value_to_add, after_value):
        target = self.find(after_value)
        if target is None:
            return # do nothing if after_value not found
        new_node = DoubleNode(value_to_add, next = target.get_next_node(),previous=target)
        if target.get_next_node() is not None:
            target.get_next_node().set_previous_node(new_node)
        else:
            self.__last_node = new_node
        target.set_next_node(new_node)
    
    
    def delete_first_node(self):
        if self.__first_node is None:
            return None
        removed = self.__first_node
        val = removed.get_value()
        self.__first_node = removed.get_next_node()
        if self.__first_node is not None:
            self.__first_node.set_previous_node(None)
        else:
            self.__last_node = None
        return val
    
    def delete_last_node(self):
        if self.__last_node is None:
            return None
        removed = self.__last_node
        val = removed.get_value()
        self.__last_node = removed.get_previous_node()
    
        if self.__last_node is not None:
            self.__last_node.set_next_node(None)
        else: 
            self.__first_node = None
        return val
    
    def delete_value(self, value):
        node = self.find(value)
        if node is None:
            return None
        val = node.get_value()
        prev_node = node.get_previous_node()
        next_node = node.get_next_node()

        if prev_node is None:
            self.__first_node = next_node
        else:
            prev_node.set_next_node(next_node)
        if next_node is None:
            self.__last_node = prev_node
        else:
            next_node.set_previous_node(prev_node)
        return val

    def forward_traverse(self):
        cur = self.__first_node
        while cur is not None:
            print (cur.get_value())
            cur = cur.get_next_node()

    def reverse_traverse(self):
        cur = self.__last_node
        while cur is not None:
            print (cur.get_value())
            cur = cur.get_previous_node()


    def __len__(self):
        count = 0
        cur = self.__first_node
        while cur is not None:
            count += 1
            cur = cur.get_next_node()
        return count
    
    def __str__(self):
        out = "["
        cur = self.__first_node
        first = True
        while cur is not None:
            if not first:
                out += " <-> "
            out += str (cur.get_value())
            first = False
            cur = cur.get_next_node()
    
        out += "]" 
        return out
      
if __name__ == "__main__":
    pass