number_list = []
for i in range(1,11):
    number_list.append(i)
print(f"Original list: {number_list}")
first_five_occurence = number_list[:5]
print(f"Extracted first five elements: {first_five_occurence}")
first_five_occurence.reverse()
print(f"Reversed extracted elements: {first_five_occurence}")