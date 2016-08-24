# Python Linked List Implementation

  This project is an implementation of a linked list data structure. It's a singly
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


**Classes**  
class Node  
  * Data:Object -> Instance Variable  
  * Next:Node -> Instance Varaible  

  * Construcuter(Object=None)  
    * Data <- Object  
    * Next = None  

class LinkedList  
  * RootNode:Node -> IV  

  * Constructer()  
    * rootNode = Node()  

  * add(Object)  
    * create a new node n = newnode(Object)  
    * lastNode = Start with root node -> iterate through linkedlist till node.next = null  
    * lastNode.next = n  

  * size()  
    * start at root node  
    * n=0  
      * loop  
        * check if next is null -> return n  
        * Got to nextnode  
        * n+1  
      * endloop  

  * remove()
    * start at the root node
    * check if the rootNode.Next is empty
      * If yes, list is empty
      * If not, adjust the removeNode to the current removeNode.Next and create a preremoveNode track the node that will have the next point removed.
        * while RemoveNode is not the last node loop
          * set the RemoveNode and PreRemoveNode
        * Once the loop breaks, we're at the end.
        * Set PreRemoveNode.Next to null to remove the last node

  * getNode(index)
    * start at the root node
    * If the list isn't currently empty, set GetNode to rootNode.Next
    * For loop with user set index
      * Set GetNode as GetNode.Next
      * Check if the current node is the last in the list, if it is, break and return
    * Endloop

    GetNode is now the desired node, return GetNode.Data

#### Example Usage  
list = LinkedList()  
size = list.size()  
list.add('jared')  
list.remove(0)  
