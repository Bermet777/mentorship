class HashMap:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        for item in self.items:
            if item[0] == key:
                item[1] = value
                return
        self.items.append([key, value])

    def get(self, key):
        for item in self.items:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key '{key}' not found.")

    def contains(self, key):
        return any(item[0] == key for item in self.items)

    def remove(self, key):
        for item in self.items:
            if item[0] == key:
                self.items.remove(item)
                return
        raise KeyError(f"Key '{key}' not found.")


if __name__ == "__main__":
    hashmap = HashMap()
    hashmap.put("apple", 5)
    hashmap.put("banana", 10)
    hashmap.put("orange", 7)
    
    print(hashmap.get("apple"))  
    print(hashmap.contains("banana"))  
    print(hashmap.contains("grape"))  
    
    hashmap.remove("orange")
    print(hashmap.contains("orange"))  
