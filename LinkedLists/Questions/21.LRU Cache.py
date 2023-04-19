class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.left , self.right = ListNode(0,0),ListNode(0,0)
        self.left.next,self.right.prev = self.right,self.left
        self.cache = {}
        
    def put(self,key,value):
        if key in self.cache:
            # remove the node
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove the least recently used node
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
    def get(self,key):
        if key in self.cache:
            # remove the node from current position
            self.remove(self.cache[key])
            # insert / make it most recently used
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self,node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        next_node.prev = node
        node.prev,node.next = prev_node,next_node
        
    
