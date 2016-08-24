# Jared Raby 2016
# Single Linkedlist implemenation in Python while not
# using array or linked list structures.

# Node class which defines what is a node and the attributes relating
class Node:
    def __init__(self, NextNode=None, NodeData=None):
        self.Data = NodeData
        self.Next = NextNode


class LinkedList:
    def __init__(self):
        self.rootNode = Node()

    def add(self, object):
        # Set the reference for the system, all adds will be in relation to this
        # root node with the new object being added to the end of the list.
        LastNode = self.rootNode
        NewNode = Node(None, object);

        # Iterate through the linkedlist. While the Node.Next attribute is not
        # null (meaning it's not the last in the list) keep iterating through
        while LastNode.Next != None:
            LastNode = LastNode.Next

        LastNode.Next = NewNode

        return

    def size(self):
        # Set the reference for the method, counts must happen in relation to the
        # root node, just as it was with the add method
        CountNode = self.rootNode
        size = 0

        # While the node.next is pointing to another node, iterate through the list
        # keeping track of the number of jumps made.
        while CountNode.Next != None:
            CountNode = CountNode.Next
            size = size + 1

        return size

    def remove(self, index):
        # Set the rootNode as reference.
        # PreRemoveNode is set to track the n-1 node in the list. This node will become
        # the new last node in the sequence, so we need to track it so we can wipe it's
        # pointer to the old node
        PreRemoveNode = self.rootNode
        
        # Checks if the root node has a next pointer, if it doesn't,
        # return that the list is empty
        if PreRemoveNode.Next == None:
            return "List is empty!"

        # Knowing that that list is not empty, we know that the next node in line
        # is possibly the one getting removed. Set up the remove node to represent tge
        # node that will be removed.
        RemoveNode = PreRemoveNode.Next

        # Check if the remove node pointer is empty. It it's not empty, we have a new 
        # set of nodes that are our preremove and remove node, so set them as such.
        i = index
        while i > 0:
            PreRemoveNode = PreRemoveNode.Next
            RemoveNode = PreRemoveNode.Next
            i = i - 1 

        # Abolish the point in the new last node, effectively removing the last node
        PreRemoveNode.Next = RemoveNode.Next

        return 

    def get(self, index): 
        # Set the reference node to iterate over
        GetNode = self.rootNode

        if GetNode.Next == None:
            return "List is empty"

        GetNode = GetNode.Next
        j = index
        
        for i in range(index):
            GetNode = GetNode.Next
            j = j - 1
            if GetNode.Next == None:
                if j > 0:
                    return "Index out of bounds"

        return GetNode.Data

    
