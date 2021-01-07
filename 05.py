#Python program to find weather the pattern present in grid or not

#Algorithm
# 1. Check if first line of pattern fits into grid. 
# 2. if it does, check for every other line of the pattern.
# 3. for every other line of pattern that checks off
    # add 1 to lineChecks once lineChecks == len(pattern) - 1 return YES
# 4. Once a line of pattern does not check off, lineChecks return to zero

'''  
        ##for i in range(len(G[0])-len(P[0])+1):

    Because if Grid[0] & Pattern[0] length are equal (0 character diff), 
    that means the code needs to check/compare at least one time.
    If Grid[0] is one character longer, that means the code needs to check twice:
    once at offset 0 to n -1, and the second one at offset 1 to n (assuming n is Grid[0] length).
    So the character count difference + 1 is the number of times you want to compare.

 '''

def search_pattern_in_grid(Grid, Pattern):
    lineChecks = 0
    for i in range(len(Grid[0])-len(Pattern[0])+1):
        for j in range(len(Grid)-len(Pattern)+1):
            if Grid[j][i:i+len(Pattern[0])] == Pattern[0]:
                for x in range(1,len(P)):
                    if Grid[j+x][i:i+len(Pattern[0])] == Pattern[x]:
                        lineChecks +=1
                        if lineChecks == len(Pattern) - 1:
                            return "YES"
                    else:
                        lineChecks = 0
    return "NO"
if __name__ == '__main__':
    Row,Col =  [int(x) for x in input().split()] 
    Grid = [input() for _ in range(Row)]
    row,col =  [int(x) for x in input().split()] 
    Pattern = [input() for _ in range(row)]
    result = search_pattern_in_grid(Grid, Pattern)

    print(result)

