# Python program to calc and print factorial of large numbers 

''' 
In Python a simple math module can used to return the desired value's factorial
            i.e., math.factorial() 

	
# importing "math" for mathematical operations 
import math 
	
x = 30
	
# returning the factorial 
print ("The factorial of 5 is : ", end ="") 
print (math.factorial(x))

****This module is written in highly optimize way,under-the-hood process is developed 
    using different technique to calc the factorial value.

#Factorial of 100 has 158 digits. Even if we use long long int to store the values that is not enough.



'''
# The idea is to use an array to store individual digits of the result

### Algorithm to find factorial(N)

# 1. Create an array of maximum size,Max with 0 or None
        # i.e., solution[None]*Max or solution[]*Max = 0
# 2. Initialize value stored in solution[] = 1 and solution_size = 1
# 3. For all numbers from i = 2 to N.
        # Update the solution_size to store result and Multiply i with solution[] and  

### Here we multiply i with every digit in solution[] from right to left digi, because it is easy to update solution[] without using extraspace and maintain the solution in reverse order.

### Multiply( solution[], i)
# 1. Initialize carry = 0.
# 2. for index from 0 to solution_size-1
        # Find value of solution[index]*i + carry
        # Update solution[index], by storing units value of product result
        # Update carry by storing other than units value or 0.
# 3. inlcude the carry value in solution[] and update the solution_size.





def factorial(N) : 
    solution = [None]*158
    # Initialize solutiona and solution size 
    solution[0] = 1
    solution_size = 1
  
    #we just multiply here every element with i
    i = 2
    # i = 2 to N
    while i <= N : 
        solution_size = multiply(i, solution, solution_size) 
        i = i + 1
      
    print ("Factorial of given number is :", end="") 
    val = solution_size-1
    while val >= 0 : 
        print(str(solution[val]),end="") 
         
        val = val - 1
          
  
# multiply() function multiplies i with the number  
# available in solution[]. solution_size is no 
# of digits present in solution[]. This function
# returns the updated value of solution_size 
def multiply(i, solution,solution_size) : 
      
    carry = 0 # Initialize carry as 0
  
    # One by one multiply n with individual 
    # digits of solution[] 
    index = 0
    while index < solution_size : 
        product = solution[index] *i + carry 
        solution[index] = product % 10; # Store units digit in solution[] 
       
        carry = product//10; # remaining in carry 
        index = index + 1
  
    # Put carry in solution[] and increase solution size 
    while (carry) : 
        solution[solution_size] = carry % 10
        
        carry = carry // 10
        solution_size = solution_size + 1
          
    return solution_size 
  
if __name__ == '__main__':
    N = int(input())
    factorial(N)