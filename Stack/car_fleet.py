from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [ (p,s) for p,s in zip(position, speed)]
        stack = []
        pairs.sort(reverse = True)
        for p,s in pairs:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
out = Solution()
res = out.carFleet(10, [4,1,0,7], [2,2,1,1])

print("This is the result: ", res)
