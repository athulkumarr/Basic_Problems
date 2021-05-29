class MinSteps:
	def coverPoints(self, A, B):
	    C = []
	    for i in range(len(A)):
	        C.append([A[i],B[i]])
        n = 0
        for i in range(len(C)-1):
            x_diff = abs(C[i][0]-C[i+1][0])
            y_diff = abs(C[i][1]-C[i+1][1])
            if x_diff > y_diff:
                n +=  y_diff + abs (x_diff - y_diff)
            else:
                n +=  x_diff + abs (x_diff - y_diff)
        return n
