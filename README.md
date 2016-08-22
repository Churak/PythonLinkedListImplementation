# PythonLinkedListImplementation

  This project is an implementation of a linked list data structure. It's a single
linked list with the following operations:
  * Add - Add a node to the end of the list containing the Object the user input
  * Remove - Removes the node at the user specified index
  * Size - Determines the size of the linked list structure
  * Get - Returns the value at a given index

**Classes**
Root node - Serves as a starting point for a linked list
    Requirement for initialization

Operations Required:
    Add - Add node to the end of the list
        Requires the data of the new node.
    Remove - Removes a specified node
        Removes the object at a given index
        Requires Index number
    Size - Determines the size of the linked list
        No user specfied arguments
    Get - Returns the value at a given index 

Classes Needed:
class Node
    Data:Object -> Instance Variable
    Next:Node -> Instance Varaible

    Construcuter(Object=None)
        Data <- Object
        Next = None

class LinkedList
    RootNode:Node -> IV

    Constructer()
        rootNode = Node()

    add(Object)
        create a new node n = newnode(Object)
        lastNode = Start with root node -> iterate through linkedlist till node.next = null
        lastNode.next = n

    size()
        start at root node
        n=0
        loop
            check if next is null -> return n
            Got to nextnode 
            n+1
        endloop

        

        
         

list = LinkedList()

size = list.size()
list.add('jared')
list.remove(0)

 
    




## Requirements
  -
  -Single Python file that is name 'LinkedList'
  -Another file that uses the linked list. 
  -Linked list implementation cannot use an array.
