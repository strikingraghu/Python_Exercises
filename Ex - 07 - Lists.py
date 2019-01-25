"""
    The most basic data structure in Python is the sequence.
    Each element of a sequence is assigned a number - its position or index.
    The first index is zero, the second index is one, and so forth.
"""

example_list = ['Ram', 8392, 944.33819, 9329338.0J, 'Suresh']
print()
print("Displaying an entire list items created above =", example_list)

# Indexing

for each_item in example_list:
    print("Item =", each_item, "& Index =", example_list.index(each_item))

# length

print("List Length [example_list] =", len(example_list))

# Getting Element (By using Index value)

print("Get Element [Uses Index Value] =", example_list.__getitem__(2))

# Reversing Elements

print("Printing Elements (Before reverse operation) =", example_list)
example_list.reverse()
print("Printing Elements (After reverse operation) =", example_list)
