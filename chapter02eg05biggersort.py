class BiggerSort:#求解下一个较大排列
    def __init__(self, nums: list[int]):
        self.nums = nums

    def nextPermutation(self) -> list[int]:
        #从右向左找到第一个降序的元素
        i=-1
        while i>-len(self.nums):
            if self.nums[i]<=self.nums[i-1]:
                i-=1
            else:
                break
        #未找到降序元素，则返回升序排列
        if i == -len(self.nums):
            return sorted(self.nums)
        #找到，则从右向左找到第一个大于nums[i-1]的元素
        j=-1
        while j>i-1:
            if self.nums[j]<self.nums[i-1]:
                j-=1
            else:
                break
        #交换nums[i-1]和nums[j-1]
        self.nums[i-1],self.nums[j]=self.nums[j],self.nums[i-1]
        return self.nums[:i]+sorted(self.nums[i:])
    #eg:
print(BiggerSort([1,2,3,4,5,3,2,1]).nextPermutation())
print(BiggerSort([5,4,3,2,1]).nextPermutation())
