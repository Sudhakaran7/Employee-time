class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stk = []
        for i, p in enumerate(prices):
            while stk and prices[stk[-1]] >= p:
                prices[stk.pop()] -= p
            stk.append(i)
        return prices
val=Solution()
n=int(input())
rows=list(map(int,input().split()))
print(*val.finalPrices(rows))
