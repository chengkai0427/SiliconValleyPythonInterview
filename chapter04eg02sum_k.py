'''
This code is to find the number of subarrays of a given array that have a sum equal to a given value k.

We can solve this problem using a sliding window approach. We maintain a window of size k and slide it over the array. At each step, we check if the sum of the current window is equal to k. If it is, we increment a counter. We also keep track of the number of times the sum of the current window has occurred so far.

To implement this approach, we can use a dictionary to keep track of the number of times the sum of the current window has occurred so far. We can initialize the dictionary with a key of 0 and a value of 1, since the sum of an empty window is 0. We can then iterate over the array and at each step, we add the current element to the sum of the window. We also update the dictionary with the new sum and the number of times it has occurred so far.

Once we have the dictionary, we can iterate over the array again and at each step, we check if the sum of the current window minus k is in the dictionary. If it is, we increment the counter by the number of times the sum of the current window minus k has occurred so far.

Here is the implementation of the above approach:
'''
from collections import defaultdict
def sum_k(arr:list[int], k:int)->int:
    sum_dict = defaultdict(int)
    count , result = 0,0
    sum_dict[0] = 1
    for num in arr:
        result += num
        sum_dict[result] += 1
        if result-k in sum_dict :
            count += sum_dict[result-k]
    return count

def sum_k_v2(arr:list[int], k:int)->int:
    count = 0
    result = 0
    pointer = 0
    for num in arr:
        result += num
        while result>k:
            result -= arr[pointer]
            pointer += 1
        if result == k:
            count += 1
    return count

if __name__ == '__main__':
    arr = [1,1,1,4,5,6,7,8,9,10]
    k =16
    print(sum_k(arr,k))
    print(sum_k_v2(arr,k))