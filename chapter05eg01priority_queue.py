'''
This code implements a function to find the minimum cost of k items from a list of items with their respective quality and price.
The function uses a priority queue to keep track of the k items with the highest quality/price ratio.
The function first sorts the items by their quality/price ratio in descending order.
Then, it iterates over the sorted items and adds the price of each item to the priority queue.
If the size of the priority queue exceeds k, it removes the item with the lowest price.
Finally, it calculates the minimum cost by multiplying the quality of the k items with their sum of prices.
'''
from queue import PriorityQueue
def min_cost(quality:list[int], prices:list[int], k:int)->float:
    pq = PriorityQueue()
    wq=sorted([(b/a,a) for a,b in zip(quality,prices)])
    qsum=0
    res=float('inf')
    for a,b in wq:
        qsum+=b
        pq.put(-b)
        if pq.qsize()>k:
            qsum+=pq.get()
        if pq.qsize()==k:
            res=min(res,a*qsum)
    return res

# Example usage:
quality = [10,20,5]
prices = [70,50,30]
k = 2
print(min_cost(quality,prices,k))# Output: 105.0

