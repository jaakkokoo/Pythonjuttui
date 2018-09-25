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
                self.head.add_after(new_first)
		
        def add_last(self, obj):
                uusi_last = ListNode(obj)
                prev_last = self.tail.predecessor
                prev_last.add_after(uusi_last)

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
