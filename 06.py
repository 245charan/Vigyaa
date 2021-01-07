# Print the sum of elements in an array

'''
We can calculate the sum of the elements in the array 
by traversing the array once, summing each element as we go.
Because this sum can be quite large, we must use a long data 
type to hold the value of our sum. A signed 32 bit integer 
uses the first bit to represent the sign of the number and 
the remaining 31 bits to represent the magnitude. The range
of a 32−bit integer is -2^31 to 2^31 -1,or[-2147483648, 2147483647].
When we add several integer values, the resulting sum might 
exceed this range. Use long in C/C++ and Java.
'''

# Algorithm
# 1. intialize array size 
# 2. intialize a list named arr
# 3. pass the array value to fun()
    # return sum use python module (or)
    # run a loop through the loop add each element into the sum variable
# 4. print the sum



def Large_array_Sum(arr):
    return sum(arr)


if __name__ == '__main__':
    arr_size = int(input()
    arr = list(map(int, input().rstrip().split()))
    result = Large_array_Sum(arr)
