# PythonLinkedListImplementation

  This project is an implementation of a linked list data structure. It's a single
linked list with the following operations:
  * Add - Add a node to the end of the list containing the Object the user input
  * Remove - Removes the node at the user specified index
  * Size - Determines the size of the linked list structure
  * Get - Returns the value at a given index

**Theory**  

Singly Linked List  
    Singly linked lists are a data structure made up of objects called _nodes_.  
    They contain several pieces of information.  
      * Data - The object being store
      * Next Pointer - A pointer which points to the next node in the list.

Root node
  * Serves as the starting point for a linked list
  * Created on linked list initilization
  * Used as a reference for all operations


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
