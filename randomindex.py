import random
from collections import defaultdict
class RandomIndex:#给定一个可能重复的整数数组，随机输出给定目标值（假定目标值必须存在于数组中）的索引。
    def __init__(self, arr: list[int]):
        self.arr = arr

    def get_random_index(self,target: int)->int:
        target_index=defaultdict(list)
        for index,target in enumerate(self.arr):
            target_index[target].append(index)
        return random.choice(target_index[target])
# Example usage:
arr = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2]
random_index = RandomIndex(arr)
print(random_index.get_random_index(2)) # Output: 1 or 3 or 9

