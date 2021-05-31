def maxSubArray(self, A):
    n = len(A)
    curr = 0
    maxx = -10000000
    for i in range(n):
        curr += A[i]
        maxx = max(maxx, curr)
        if (curr<0):
            curr = 0
    return maxx;

A = [2, 3, 4, -1, 10, -11, 9]
print(maxSubArray(A))
