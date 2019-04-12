from Node import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None # helps to improve insert performance

    def traverse(self, msg=None):
        if (msg != None):
            print(msg)
        node=self.head
        while node != None:
            print(node.val, end=" ")
            node = node.next
        print()

    def traverseBackward(self, msg=None):
        if (msg != None):
            print(msg)
        node=self.last
        while node != None:
            print(node.val, end=" ")
            node = node.prev
        print()

    def insert(self, node):
         if (self.head == None):
             self.head=node
             self.last=node
         else:
             node.prev=self.last
             self.last.next=node
             self.last=node

    def count(self):
        count=0
        node=self.head
        while node != None:
            count += 1
            node = node.next
        return count

    def delete(self, val, deleteAll=True): # default to delete all matching values
        node=self.head
        if node == None:
            return

        prevNode=None
        itIsHead=True
        while node != None:
            if (val == node.val):
                print("\nremoved node val="+str(val)+"\n")
                if (itIsHead == True): ### del as head
                    if (node.next.next != None):
                        node.next.prev=None

                    self.head = node.next
                else:
                    if (node.next == None): # The last node
                        self.last=prevNode
                    else:
                        node.next.prev=prevNode
                    prevNode.next=node.next
            else:
                itIsHead=False

            if (deleteAll == False):
                  break
            else:
                prevNode=node

            node=node.next

######################################################################
# Test all scenarios
# 1) delete head
# 2) delete in the middle
# 3) delete tail
# 4) delete multiple occurrences
# 5) traverseBackward from the tail

ll=DoubleLinkedList()

ll.insert(Node(1))
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(1))
ll.insert(Node(3))
ll.traverse("Original List")
ll.traverseBackward("Original List Traverse Backward")


ll.delete(2)
#ll.delete(1, False)
#ll.delete(1)
#ll.delete(3)

### output ###
#Original List
#1 1 2 1 3
#Original List Traverse Backward
#3 1 2 1 1

#removed node val=2

#Final List
#1 1 1 3
#Traverse Backward Final List
#3 1 1 1

ll.traverse("Final List")
ll.traverseBackward("Traverse Backward Final List")

