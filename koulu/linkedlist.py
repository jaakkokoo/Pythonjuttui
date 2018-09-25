class ListNode:
    
        """

        The LinkedList uses ListNode objects to store added values.

        This class will not be tested by the grader.

        Attributes:

        obj: Any object that need to be stored.

        follower: A ListNode object that follows this (self) ListNode object

        in the linked list.

        predecessor: A ListNode object that precedes this (self) ListNode object

        in the linked list.

        """

        def __init__(self, obj):

                """Initialize a list node object with the value obj."""

                self.obj = obj #data

                self.follower = None #seuraava

                self.predecessor = None #jalkimmainen

        def add_after(self, node):

                """Adds node 'node' as the follower of this node."""
                tmp = self.follower

                self.follower = node

                node.predecessor = self

                node.follower = tmp

                if tmp:

                    tmp.predecessor = node

        def remove_after(self):

                """Removes the follower of this node."""

                if self.follower:

                    self.follower = self.follower.follower

                if self.follower:

                    self.follower.predecessor = self

class LinkedList:

        """

        An implementation of a doubly linked list that uses ListNode objects

        to represent nodes in the list. List indexes start from zero.

        The list contains one head and one tail guardian node with the values None.

        These can be used to check if the head or tail has been reached.

        The guardian nodes should not be included when counting the size of the list.

        """

        def __init__(self):

                """Initialize the linked list."""

                self.ListNode = ListNode

                self.head = self.ListNode(None)

                self.tail = self.ListNode(None)
                # An empty list should only have one head node followed by a tail node

                self.head.add_after(self.tail)

        def _get_at(self, n):

                i = 0
                walker = self.head.follower
                if walker == self.tail:
                    pass
                while i < n:
                        walker = walker.follower
                        i += 1
                return walker
			
                """Return the node at position 'n'."""
        def add_first(self, obj):
                new_first = ListNode(obj)
                #last_first = self._get_at(1)
                self.head.add_after(new_first)
                #new_first.add_after(last_first) !!!!
		
		#if new_first.follower.obj == None:
		#	new_first.add_after(self.tail)
		#else:
		#	new_first.add_after(self._get_at(2))
		
        def add_last(self, obj):
                #in = self.get_size()
                #prev_last = self._get_at(n)
                uusi_last = ListNode(obj)
                #nthminusyks = self._get_at(n-1)
                #nthminusyks.add_after(uusi_nth)
                #uusi_nth.add_after(original_nth)
                
                
                prev_last = self.tail.predecessor
                #uusi_last = ListNode(obj)
                prev_last.add_after(uusi_last)
		
		#linkitetaan tail
                #uusi_last.add_after(self.tail)	
		
		      

                """Add the object 'obj' as the last node."""


        def add_position(self, n, obj):
                uusi_nth = ListNode(obj)
                nth_node = self._get_at(n)
                if nth_node == self.tail:
                    self.add_last(obj)
                elif nth_node == self.head:
                    self.add_first(obj)
                else:
                    nth_node.predecessor.add_after(uusi_nth)
               # original_nth = self._get_at(n)
               # uusi_nth = ListNode(obj)
               # nthminusyks = self._get_at(n-1)
               # nthminusyks.add_after(uusi_nth)
               # uusi_nth.add_after(original_nth)
		

                """Insert the object 'obj' as the 'n'th node."""


        def remove_position(self, n):
                """Remove the node at the 'n'th position."""

                predecessor = self._get_at(n).predecessor

                if predecessor:

                    predecessor.remove_after()

        def get_position(self, n):

                """Return the value of the node at the 'n'th position or None

                if there is no node at that position."""

                node = self._get_at(n)

                return node.obj if node else None

        def get_size(self):
                i = 0
                walker = self.head
                while walker.follower != self.tail:
                        i += 1
                        walker = walker.follower
                return(i)
                """Return the number of objects in the list."""

'''
JaakonLista = LinkedList()
JaakonLista.add_first("kakka")
print("eka:",JaakonLista._get_at(0))
JaakonLista.add_last("pylly")
print("vika:",JaakonLista._get_at(1))
print(JaakonLista(ListNode))

from sys import exit as proper_exit
proper_exit()

eka = 'yksi'
toka = 'kaksi'
kolmas = 'kolme'
#LinkedList.toka.add_last()
#LinkedList.kolmas.add_position(1)

dev_1 = ListNode('testi')
dev_2 = ListNode('toinentesti')
dev_3 = ListNode('kolmastesti')

#LinkedList.add_first(dev_1)
print("dev_1")
print("kaks ==", dev_1.obj)
print(dev_1.follower)
print(dev_1.predecessor)
print("dev_2")
print(dev_2.obj)
print(dev_2.follower)
print(dev_2.predecessor)
print("dev_3")
print(dev_3.obj)
print(dev_3.follower)
print(dev_3.predecessor)
#LinkedList.obj(dev_1)
#LinkedList.add_first()


LinkedList.add_first(LinkedList,dev_1)
#dev_2.add_after(dev_1)
#dev_3.add_after(dev_2)
#dev_1.add_after(dev_3)
#dev_1.add_after(dev_2)
print("dev_1")
print(dev_1.obj)
print(dev_1.follower)
print(dev_1.predecessor)
print("dev_2")
print(dev_2.obj)
print(dev_2.follower)
print(dev_2.predecessor)
print("dev_3")
print(dev_3.obj)
print(dev_3.follower)
print(dev_3.predecessor)
print(LinkedList.get_size())
#print(dev_1.LinkedList.head.obj)



'''
