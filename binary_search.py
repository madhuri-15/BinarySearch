#! Python3
# Python program to search element index in the given array using a binary search algorithm.



## Recursive method
def binary_search(value, arr):

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        if arr[0] == value:
            return "0"
    else:
        mid_index = len(arr) // 2
        mid_value = arr[mid_index]

        if mid_value == value:
            return mid_index
          
        elif mid_value > value:
            return binary_search(value, arr[:mid_index])
          
        elif mid_value < value:
            return binary_search(value, arr[mid_index:])
      
        else:
            return None

          
          
          
          
if __name__ == '__main__':

    arr= [1, 2, 3, 4, 5, 6, 8]
    value = 4
    result = binary_search(value, arr)
    
    if result:
        print(f"The value {value} is present at index {result}.")
    else:
        print(f"The value {value} is not present in the array.")

## Output: The value 4 is present at index 3.
