def order_and_eliminate_duplicates(input_list):
    input_list.sort()

    i = 0
    while i < len(input_list) - 1:
        if input_list[i] == input_list[i + 1]:
            del input_list[i]
        else:
            i += 1

original_list = [4, 2, 2, 1, 3, 4, 1, 5]

order_and_eliminate_duplicates(original_list)

print(original_list)
