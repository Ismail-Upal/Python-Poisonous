# index    0    1   2   3   4   5
numbers = [23, 34, 53, 63, 43, 32] # list
# indes   -6   -5  -4  -3  -2  -1   

print(numbers[3], numbers[-3])
# list(start : end )
print(numbers[2:6])# start from the start index and stops before the end index

# list(start : end : step)
print( numbers[ 1: 6: 2])
print( numbers[ 1: 6: -1])
print( numbers[ 6: 1: -1])
print( numbers[2: ])
print( numbers[ :6])
print( numbers[ : ])#shortcut to copy a list

print( numbers[ : : -1]) #shortcut to reverse a list

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].