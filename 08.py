#Program to calc weather Kangaroos meet or not
'''
#Function that accepts four parameters called x1, v1, x2, and v2.
#If both the Kangaroos meets at same spot with same jumps then print YES
#If both the Kangaroos have same speed then print NO
#If both the kangaroos never meets then print NO
'''
#Algorithm

#Both intial points are different they need to follow 2 conditions
    # Both speeds should be different and unique 
    # Difference between speeds divide the total distance between initial points.
            # Diference between speed = V1 - V2 and V2 - V1
            # Difference between total distace = X2 - X1 and X1 - X2


def can_kangaroos_meet(x1, v1, x2, v2): 
  
    return ( (v1 > v2 and (x2 - x1) % (v1 - v2) == 0)  
         or (v2 > v1 and (x1 - x2) % (v2 - v1) == 0)) 
  
  
if __name__ == '__main__':
    x1v1x2v2 = input().split()

    x1 = int(x1v1x2v2[0])

    v1 = int(x1v1x2v2[1])

    x2 = int(x1v1x2v2[2])

    v2 = int(x1v1x2v2[3])

    if(can_kangaroos_meet(x1, v1, x2, v2)): 
        print("Yes") 
    else: 
        print("No") 