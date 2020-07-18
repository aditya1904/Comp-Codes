"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
def flattenchild(current, child, current_next):
    tail = child
    while(tail.next):
        tail = tail.next
    tail.next = current_next
    child.prev = current
    current.next = child
    if(current_next):
        current_next.prev = tail
    current.child = None
    return current

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        current = head
        while(current):
            if(current.child):
                current = flattenchild(current, current.child, current.next)
            else:
                current = current.next
        return head