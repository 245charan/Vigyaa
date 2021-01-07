#find and print the number of times she breaks her record for most and least points scored during the season.

#Algorithm 

# 1. Initialize the Score and take input()
# 2. call the function by passing score as a parameter
        # 2.1 Initialize the min and max variable with the first element    
            # min = max = score[0]
        # 2.2 Traverse through the score array
            # if the current value is greater than max then update max_count++ and max as current element
            # if current value is less than min update min_count++ and min as current element
        # return max_count and min_count
# 3. print max count and min count seperatly 

def best_and_worst(score):
    min = max = score[0]
    min_count = max_count = 0
    for i in score[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    return max_count, min_count


n = int(input())
score = list(map(int, input().split()))
print(best_and_worst(score))
