# Testing documentation and tests for the linklist structure implementation.
# Jared Raby 20126


# Import the Linkedlist and Node classes to implement the test cases.
from linkedlist import LinkedList
from linkedlist import Node

import string

def main():
    
    list = LinkedList()

    list.add("Apples")
    list.add("Bananas")
    list.add("Cookies")

    print 'The list contains ' + str(list.size()) + ' items.'
    print str(list.get(0)) + ', ' + str(list.get(1)) + ', ' + str(list.get(2))

    print 'Remove item from list at index 1'
    list.remove(1)
    print str(list.get(0)) + ', ' + str(list.get(1))
    print 'The list contains ' + str(list.size()) + ' items.'


if __name__ == "__main__":
    main()
