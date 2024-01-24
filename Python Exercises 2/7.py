class listas:
    def __init__(self, data):
        self.data = data

    def add_element(self, element):
        self.data.append(element)

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

data = [1, 2, 3, 4, 5]
my_list = listas(data)

my_list.add_element(6)

print("Sum:", my_list.sum())
print("Max:", my_list.max())
print("Min:", my_list.min())
print("Avg:", my_list.avg())
