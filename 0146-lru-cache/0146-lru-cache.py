# Design LRU Cache

# Cache has capacity
# Store (key, value) in cache
# Get the value for a particular key from the cache
# Put a new (key,value) into cache
# If key there -> put new value for it
# If key, value added > capacity of cache: remove LRU (key, value)

# Hashmap to be used
# to keep and order and add and remove from anywhere in O(1) time-> DLL
# To keep track of LRU and MRU: left and right pointers

# class for creating nodes for linked list
# class for lru cache with the functions
# get function -> gets the key value if present, moves LRU node to right
# put function -> if key to be put exists -> remove it, add new node (key, val), check if capacity exceeded -> remove LRU if so
# to move LRU, helper functions
# remove function -> for node to be removed: point prev to next node, and vice versa
# insert function -> node to be inserted on right- point rightmost node to it and backward too

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next= self.prev = None
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, Node):
        prev = self.right.prev
        nxt = self.right
        nxt.prev = Node
        prev.next = Node
        Node.next = self.right
        Node.prev = prev
        
        
        
    def remove(self, Node):
        prev = Node.prev
        nxt = Node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,val)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]