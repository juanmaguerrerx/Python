class listas:
    def __init__(self, data):
        self.data = data

    def most_repeated(self):
        if not self.data:
            return None

        most_common = self.data[0]
        max_count = self.data.count(most_common)

        for item in self.data:
            count = self.data.count(item)
            if count > max_count:
                most_common = item
                max_count = count

        return most_common

# Example usage
data = [1, 2, 3, 2, 4, 3, 4, 3, 5]
my_list = listas(data)

most_common_element = my_list.most_repeated()
print("Most Repeated Element:", most_common_element)
