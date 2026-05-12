class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0
        self.used = []
        self.storage = {}
        

    def get(self, key: int) -> int:
        if key in self.storage:
            self.used.remove(key)
            self.used.append(key)
            return self.storage[key]
        else:
            return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.used.remove(key)
            self.used.append(key)
            self.storage[key] = value
        else:
            if self.capacity == self.curr_capacity:
                last_used_key = self.used[0]
                self.used.remove(last_used_key)
                self.storage.pop(last_used_key)
                self.storage[key] = value
                self.used.append(key)
            else:
                self.storage[key] = value
                self.used.append(key)
                self.curr_capacity += 1

        
