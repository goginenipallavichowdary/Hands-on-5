import math

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_min_heap(self, arr):
        self.heap = arr.copy()
        for i in range(self.parent(len(self.heap) - 1), -1, -1):
            self.heapify(i)

    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self.heapify_up(parent)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return min_val

    def __str__(self):
        return str(self.heap)

# Example usage
def main():
    # Integer example
    int_heap = MinHeap()
    int_data = [4, 10, 3, 5, 1]
    print("Integer data:")
    print("Initial data:", int_data)
    int_heap.build_min_heap(int_data)
    print("Heap after build_min_heap:", int_heap)
    int_heap.insert(2)
    print("Heap after inserting 2:", int_heap)
    min_val = int_heap.pop()
    print("Popped value:", min_val)
    print("Heap after popping:", int_heap)
    print()

    # Float example
    float_heap = MinHeap()
    float_data = [4.5, 10.2, 3.8, 5.1, 1.7]
    print("Float data:")
    print("Initial data:", float_data)
    float_heap.build_min_heap(float_data)
    print("Heap after build_min_heap:", float_heap)
    float_heap.insert(2.3)
    print("Heap after inserting 2.3:", float_heap)
    min_val = float_heap.pop()
    print("Popped value:", min_val)
    print("Heap after popping:", float_heap)
    print()

    # Custom data structure example
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __lt__(self, other):
            return self.age < other.age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    person_heap = MinHeap()
    persons = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("David", 28)
    ]
    print("Person data:")
    print("Initial data:", persons)
    person_heap.build_min_heap(persons)
    print("Person heap after build_min_heap:", person_heap)
    person_heap.insert(Person("Eve", 22))
    print("After inserting Eve (22):", person_heap)
    youngest = person_heap.pop()
    print("Youngest person (popped):", youngest)
    print("Person heap after popping:", person_heap)

if __name__ == "__main__":
    main()
