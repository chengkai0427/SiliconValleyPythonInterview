'''
标签中的最大值
有一组项目：第i个项目具有值value[i]和标签lable[i]。选择这些项目的子集S，
满足：S的大小最大为num_wanted;并且对于每个标签L，带有标签L的S中的项目数最多为use_limit。
返回子集S的最大可能和。
'''
from collections import defaultdict
def largest_value_of_label(value:list[int], label:list[str], num_wanted:int, use_limit:int)->int:
    largest_sum = 0
    dict_label = defaultdict(int)
    for v,l in sorted(zip(value,label), reverse=True):
        if num_wanted>0 and dict_label[l] < use_limit:
            num_wanted -= 1
            largest_sum += v
            dict_label[l] += 1
        elif not num_wanted:
            break
    return largest_sum
#test
value = [1,2,3,4,5,6,7,8,9,10]
label = ['a','a','b','b','c','c','d','e','e','e']
num_wanted = 4
use_limit = 2
print(largest_value_of_label(value, label, num_wanted, use_limit)) #output: 27