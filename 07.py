# Print the minimum and maximum sum can be formed from a array 

#ALgorithm

## Using Dequeue Data Structure and sliding window concept we can solve this problem.
#  The queue will store indexes of useful elements in every window. 
# 1. In deque 'Decs' we maintain decreasing order of 
#    values from front to rear 
# 2. In deque 'Incs we  maintain increasing order of 
#    values from front to rear

# 3. First window size K
  # 3.1 For deque 'Decs', if current element is greater 
      # than rear end element, we remove rear while 
      # current is greater.
  # 3.2 For deque 'Incs', if current element is smaller 
      # than rear end element, we just pop it while 
      # current is smaller.
  # 1.3 insert current element in both deque 'Decs' 'Incs'

# 4. After step 1, front of 'Decs' contains maximum element
   # of first window and front of 'Incs' contains minimum 
   # element of first window. Remaining elements of Decs
   # and Incs may store maximum/minimum for subsequent 
   # windows.

# 5. After that we do traversal for rest array elements.
  # 5.1 Front element of deque 'Decs' is greatest and 'Incs' 
      # is smallest element of previous window 
  # 5.2 Remove all elements which are out of this 
      # window [remove element at front of queue ]
  # 5.3 Repeat steps 1.1 , 1.2 ,1.3 

# 6. Return sum of minimum and maximum element of all 
   # sub-array size k.


from collections import deque 
  
# Returns Sum of min and max element of all subarrays 
# of size k 
def min_max_sum(arr, Size , k): 
  
    Sum = 0 # Initialize result 
  
    
    Incs = deque() 
    Decs = deque() 
  
  
    # Process first window of size K 
  
    for i in range(k): 
          
        # Remove all previous greater elements 
        # that are useless. 
        while ( len(Incs) > 0 and arr[Incs[-1]] >= arr[i]): 
            Incs.pop() # Remove from rear 
  
        # Remove all previous smaller that are elements 
        # are useless. 
        while ( len(Decs) > 0 and arr[Decs[-1]] <= arr[i]): 
            Decs.pop() # Remove from rear 
  
        # Add current element at rear of both deque 
        Decs.append(i) 
        Incs.append(i) 
  
     
    for i in range(k, Size): 
          
    
        Sum += arr[Incs[0]] + arr[Decs[0]] 
  
        # Remove all elements which are out of this 
        # window 
        while ( len(Incs) > 0 and Incs[0] <= i - k): 
            Incs.popleft() 
        while ( len(Decs) > 0 and Decs[0] <= i - k): 
            Decs.popleft() 
  
        # remove all previous greater element that are 
        # useless 
        while ( len(Incs) > 0 and arr[Incs[-1]] >= arr[i]): 
            Incs.pop() # Remove from rear 
  
        # remove all previous smaller that are elements 
        # are useless 
        while ( len(Decs) > 0 and arr[Decs[-1]] <= arr[i]): 
            Decs.pop() # Remove from rear 
  
        # Add current element at rear of both deque 
        Decs.append(i) 
        Incs.append(i) 
  
    # Sum of minimum and maximum element of last window 
    Sum += arr[Incs[0]] + arr[Decs[0]] 
  
    return Sum
  

if __name__ == '__main__':
    Size = int(input()) 
    arr = [input() for _ in range(Size-1)]
    k = 3
    print(min_max_sum(arr, Size, k))