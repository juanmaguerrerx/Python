class listas:
    def __init__(self, data):
        self.data = data

    def add_elements(self, elements):
        self.data.extend(elements)

    def sum(self):
        total = 0
        for item in self.data:
            total += item
        return total

    def max(self):
        max_val = self.data[0]
        for item in self.data:
            if item > max_val:
                max_val = item
        return max_val

    def min(self):
        min_val = self.data[0]
        for item in self.data:
            if item < min_val:
                min_val = item
        return min_val

    def avg(self):
        if len(self.data) == 0:
            return 0
        total = self.sum()
        return total / len(self.data)

# Example usage
data = [1, 2, 3, 4, 5]
my_list = listas(data)

# Add elements from a second list
second_list = [6, 7, 8]
my_list.add_elements(second_list)

print("Sum:", my_list.sum())
print("Max:", my_list.max())
print("Min:", my_list.min())
print("Avg:", my_list.avg())
