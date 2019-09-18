#Myungho Sim
#implement LRU cache Work in progress
class ListNode:
    def __init__(self, n:int):
        self.val = n
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {} #stores ListNode 
        self.head = None
        self.tail = None
        self.cap = capacity
        self.count = 0
    def get(self, key: int) -> int:
        try:
            node = self.arr[key]
            return node.val
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        #check if key already in map
        if self.head is None:
            self.head = ListNode(value)
            self.map[value] = self.head
            self.tail = self.head
            self.count+=1
        else:
            try:
                #check if node already in map. 
                node = map[key]
                if node!=self.head:
                    #set prev next to next
                    prev = node.prev
                    prev.next = node.next
                    #put node to the front
                    node.next =  self.head
                    self.head = node
                self.count+=1
            except:
                #check if cache full
                #if full, evict least used. 
                if self.count==self.cap:
                    prev = self.tail.prev
                    prev.next = None
                    self.tail = None
                    node = ListNode(value)
                    self.tail = node
                    prev.next = node
                #if not full, add to listnode and map
                else:
                    node = ListNode(value)
                    self.tail.next = node
                    self.tail = node
                    self.count+=1
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
