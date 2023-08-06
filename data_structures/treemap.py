class TreeMap:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        for i, item in enumerate(self.items):
            if key == item[0]:
                self.items[i] = (key, value)
                return
            elif key < item[0]:
                self.items.insert(i, (key, value))
                return
        self.items.append((key, value))

    def get(self, key):
        for item in self.items:
            if key == item[0]:
                return item[1]
        raise KeyError(f"Key '{key}' not found.")

    def contains(self, key):
        for item in self.items:
            if key == item[0]:
                return True
        return False

    def remove(self, key):
        for i, item in enumerate(self.items):
            if key == item[0]:
                self.items.pop(i)
                return
        raise KeyError(f"Key '{key}' not found.")


if __name__ == "__main__":
    treemap = TreeMap()
    treemap.put("apple", 5)
    treemap.put("banana", 10)
    treemap.put("orange", 7)

    print(treemap.get("apple")) 
    print(treemap.contains("banana"))  
    print(treemap.contains("grape"))  

    treemap.remove("orange")
    print(treemap.contains("orange"))  
