class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")
    
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")

# Testing the VerboseList class
if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)

