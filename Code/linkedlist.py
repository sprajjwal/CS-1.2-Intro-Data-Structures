#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) because we maintain the size of list as a variable """
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we have access to the tail """
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) always because we have access to head of 
        the list."""
        new_node = Node(item)
        if self.head:
            new_node.next = self.head
        else: 
            self.tail = new_node
        self.head = new_node
        self.size += 1

        

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if the item at node satisfies or if the list
        is empty. Worst case running time: O(n)  if the item we are looking for
        is the last item."""
        if not self.head:
            return None
        else:
            cur_node = self.head
            while cur_node:
                if quality(cur_node.data):
                    return cur_node.data
                cur_node = cur_node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) when deleting at head
        Worst case running time: O(n) when deleating from tail"""
        if not self.head:
            raise ValueError(f"Item not found: {item}")
        if self.head.data == item: # if matching item is at head
            if self.head == self.tail: # if head == tail, list is of size 1
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return
        else: # if item is not at head
            cur_node = self.head.next
            prev = self.head
            while cur_node:
                if cur_node.data == item:
                    if cur_node == self.tail: # if item is at tail
                        self.tail = prev
                        prev.next = None
                    else:
                        prev.next = cur_node.next
                    self.size -= 1
                    return
                prev = cur_node
                cur_node = cur_node.next

        raise ValueError(f"Item not found: {item}")

    def replace(self, item, replace_with):
        """Replace the item from linked list with replace_with, or raise ValueError.
        Best case running time: O(1) if replacing at head
        Worst case running time: O(n) when replacing at tail."""
        cur_node = self.head
        while cur_node:
            if cur_node.data == item:
                cur_node.data = replace_with
                return
        raise ValueError(f"Item not found: {item}")
                    

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
