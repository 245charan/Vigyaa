# Python program to convert the  3 x 3 matrix .
# to magic square at minimal cost

'''
Find all 3x3 magic squares and for each one compute the cost of changing matrix into a known magic square.
'''

# 1. To generate all possible magicSqaure matrix using the below mentioned brute force condition 
        #l = [[a,b,c,d,e,f,g,h,i] for a in range(1,10) for b in range(1,10) for c in range(1,10) for d in range(1,10) for e in range(1,10) for f in range(1,10) for g in range(1,10) for h in range(1,10) for i in range(1,10) if a+b+c==15 and d+e+f==15 and g+h+i==15 and a+d+g==15 and b+e+h==15 and c+f+i==15 and a+e+i==15 and c+e+g==15 and len(set([a, b,c,d,e,f,g,h,i]))==9]
        # print = l
# 2. pass the current 3x3 matrix to fun() 
# 3. use two varialbes to store the minimum cost value
        # i.e., mincost = 9999, cost
# 4. calc the absolute difference between the currentmatrix and magicSqaure and add the diff to the cost 
        
# 5. Update the value of mincost
        # i.e.,mincost = min(mincost,cost)
    #print mincost


    
def convert_to_MagicSquare(Matrix):
    #print(Matrix)
    l=[[[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]] ]
    #print(l)
    mincost=9999
    for i in range(8):
        c=0
        for j in range(3):
            for k in range(3):
                #print(l[1][2])
                cost = cost +abs(l[i][j][k]-Matrix[j][k])# calc the abs diff between intput matrix and existing MagicSquare and add to the cost value
        mincost = min(mincost,cost)
    print(mincost)
    
 
if __name__ == '__main__':
    Matrix = []
    for _ in range(3):
        Matrix.append(list(map(int, input().rstrip().split())))
    convert_to_MagicSquare(Matrix)
    