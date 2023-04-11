class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        start , end = 0,1
        res = []
        while i < len(firstList) and j < len(secondList):
            a_overlaps_b = firstList[i][start] >= secondList[j][start] and firstList[i][start] <= secondList[j][end]
            b_overlaps_a = secondList[j][start] >= firstList[i][start] and secondList[j][start] <= firstList[i][end]
            if a_overlaps_b or b_overlaps_a:
                res.append([max(firstList[i][start],secondList[j][start]),min(firstList[i][end],secondList[j][end])])
            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1
        return res
# TC : O(N+M)
# SC : O(N)