class LLNode:
    def __init__(self, n = None):
        self.data = n
        self.next = None

class SLL:
    def __init__(self, n = None):
        self.Head = None
        
if __name__ == '__main__':
    ll = SLL()
    ll.Head = LLNode()
    ll.delete(1)
    ll.insertleft(1)
    ll.insertright(2)
    ll.printall()
    ll.delete(1)
