class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = one = 0
        result = float('inf')
        res = ""
        for right in range(len(s)):
            if s[right] =='1':
                one+=1
            while left < right and one > k:
                one = one - 1 if s[left] == '1' else one
                left += 1
                
            while s[left] == '0' and one == k:
                left+=1

            if one == k:
                current = s[left:right+1]
                if not res:
                    res = current
                elif len(current) < len(res):
                    res = current
                elif len(current) == len(res) and current < res:
                    res = current
                
        return res