class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       #monotincolly decreasing queue 
       res = []
       l = r = 0
       q = collections.deque()

       while r < len(nums):
        #pop smaller values in queue
        #loop keeps queue in descending order
        '''
        as r grows it the loops checks if the right most of queue is smaller than r and pops if it is and continuously appends r, the queue stores the index of the values and l>q[0] pops whenevrer window increases
        '''
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
            
        if (r + 1) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1

       return res