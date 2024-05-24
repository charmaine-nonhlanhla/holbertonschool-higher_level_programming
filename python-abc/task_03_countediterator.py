class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # Fetch the next item
        self.counter += 1           # Increment the counter
        return item

    def get_count(self):
        return self.counter

# Testing the CountedIterator class
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")

