### Task 13: Implement Binary Search
# python
def binary_search(arr, target):
    ### arr length
 left, right = 0, len(arr) - 1
 while left <= right:
### find middle index
 mid = (left + right) // 2
 ### value terget mil jaye to return mid
 if arr[mid] == target:
 return mid
 elif arr[mid] < target:
 left = mid + 1
 else:
 right = mid - 1
 return -1
 ### print all number
print(binary_search([1, 3, 5, 7, 9], 7))

