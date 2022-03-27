from heapq import heappush, heappop

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    
    def binarySearch(row):
      left, right = 0, len(row)
      while left < right:
        mid = left + (right-left)//2
        if row[mid] == 1:
          left = mid + 1
        else:
          right = mid
      return left
    
    maxHeap = []
    for i in range(len(mat)):
      strength = binarySearch(mat[i])
      heappush(maxHeap, (-strength, -i, i))
      
      while len(maxHeap) > k:
        heappop(maxHeap)

    res = [0]*k
    for i in range(k-1, -1, -1):
      res[i] = heappop(maxHeap)[2]    
    return res