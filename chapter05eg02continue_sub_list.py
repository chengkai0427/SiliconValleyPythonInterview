#将一个升序整数列表分割成若干个连续整数的子列表，每个子列表的长度至少为n。如不能分割，则返回'不能按要求分割'。
from typing import Union,Literal
import heapq
def split_list(splited:list[int], n:int)->Union[list[list[int]],Literal['不能按要求分割']]:
    length=1
    before=heapq.heappop(splited)
    sub_list = [[before]]
    while splited:
        after=heapq.heappop(splited)
        if after-before==1:
            length+=1
            before=after
            sub_list[-1].append(before)
        else:
            if length>=n:
                before=after
                sub_list.append([before])
                length=1
            else:
                return '不能按要求分割'
    if length>=n:
        return sub_list
    else:
        return '不能按要求分割'
if __name__=="__main__":
    splited=[1,2,3,4,4,5,6,6,7,8,9,10]
    n=3
    print(split_list(splited,n))
