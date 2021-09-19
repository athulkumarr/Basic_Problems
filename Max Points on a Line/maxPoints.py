def maxPoints(self, points):
        n = len(points)
        if n<=2:
            return n
        m = 0
        for i in range(n):
            slope = {}
            for j in range(n):
                if i!=j:
                    if points[i][0]==points[j][0]:
                        slope['v'] = slope.get('v',0)+1
                    elif points[i][1]==points[j][1]:
                        slope['h'] = slope.get('h',0)+1
                    else:
                        s = 1.0*(points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                        slope[s] = slope.get(s,0)+1
            if len(slope)>0:
                m = max(m, max(slope.values())+1)
        return m
