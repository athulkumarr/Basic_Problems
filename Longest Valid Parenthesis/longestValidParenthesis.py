def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        max_ = 0
        for i in range(1, len(s)):
            if s[i] ==')':
                if s[i-1]== '(':
                    dp[i] = (dp[i-2]+2) if i>1 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i - dp[i - 1] - 2]+2 if (i-dp[i-1] >1) else 2)
            max_ = max(max_, dp[i])
                                        
        return max_
