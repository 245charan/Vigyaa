# 10th Code on the  Assignment

# Input of the Sighting array
Arr = [int(x) for x in input().split()]
Arr.sort()

# Create a dictionary to track the count of each of them
count_map = {}
for num in Arr:
    if num in count_map:
        count_map[num] += 1
    else:
        count_map[num] = 1

print(count_map)

print(max(count_map, key= lambda x: count_map[x]))