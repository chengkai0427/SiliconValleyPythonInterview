class OneOfBinarySums:#求解二进制数组中最长连续1的个数
    def __init__(self, nums:list[int]):
        if nums.count(0)+nums.count(1)!=len(nums):
            raise ValueError("二进制数组中只能包含0和1")
        self.nums=nums

    def longestConsecutiveOnes(self)->int:
        max_len=0
        length1=0
        for num in self.nums:
            if num:
                length1+=1
            else:
                max_len=max(max_len,length1)
                length1=0
        return max(max_len,length1)

if __name__=="__main__":
    nums=[1,1,0,0,1,1,0,1,1,1]
    obj=OneOfBinarySums(nums)
    print(obj.longestConsecutiveOnes())#输出：3