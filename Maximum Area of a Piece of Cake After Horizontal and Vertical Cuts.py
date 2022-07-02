# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        H = sorted([0] + horizontalCuts + [h])
        V = sorted([0] + verticalCuts + [w])
        return max(j-i for i,j in zip(H, H[1:])) * max(j-i for i,j in zip(V, V[1:])) % (10**9 + 7)