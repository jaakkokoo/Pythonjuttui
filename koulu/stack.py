from linkedlist import LinkedList
class Stack:
    """
    An implementation of a stack structure which utilizes the LinkedList class.
    Attributes:
    stack (LinkedList): A linked list that is used to store the objects added into the stack.
    """

    def __init__(self):
        """Initialize the stack."""
        self.stack = LinkedList()

    def push(self, obj):
        self.stack.add_first(obj)
        """Add the object 'obj' to the stack."""
        #raise NotImplementedError('Fix me!')
   
    def pop(self):
        top_of_stack = self.stack._get_at(0)
        self.stack.remove_position(0)
        return top_of_stack.obj
        """Return and remove the newest (previously added) object from the stack."""
       # raise NotImplementedError('Fix me!')
   
    def top(self):
        top_of_stack = self.stack._get_at(0)
        return top_of_stack.obj
        """Return the newest (previously added) object."""
        #raise NotImplementedError('Fix me!')
   
    def is_empty(self):
        if self.stack.get_size() == 0:
            return True
        else:
            return False
        """If stack has no objects, return True, else return False."""
        #raise NotImplementedError('Fix me!')
