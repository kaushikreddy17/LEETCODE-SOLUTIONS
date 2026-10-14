class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ""
        cur = sum
        while cur > 0:
            digit = min(9, cur)
            ans += str(digit)
            cur -= digit
        i = num - len(ans)
        if i < 0:
            return ""
        while i > 0:
            ans += '0'
            i -= 1
        return ans