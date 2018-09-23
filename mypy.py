# Returns True if A contains item and False otherwise
def binary_search(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
       # your code goes here
        #A[:middle] is a copy of the elements of A to the left of middle
            return binary_search(A[:middle], item)
        else:
        #A[middle+1:] is a copy of the elements of A to the right of middle
            return binary_search(A[middle + 1:], item)
list = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search(list, 4))
print(binary_search(list, 42))