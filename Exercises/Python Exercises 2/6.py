original_list = [4, 2, 2, 1, 3, 4, 1, 5]

sorted_list = original_list.copy()
sorted_list.sort()

result_list = []

while sorted_list:
    current_item = sorted_list.pop(0)
    result_list.append(current_item)
    while sorted_list and sorted_list[0] == current_item:
        sorted_list.pop(0)

print(result_list)
