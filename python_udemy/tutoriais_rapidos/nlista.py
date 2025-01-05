import heapq


my_list = [20, 43, 91, 2, 10, 34, 0, 88, 58, 23, 44, 2]

print(heapq.nlargest(5, my_list))
print(heapq.nsmallest(5, my_list))
