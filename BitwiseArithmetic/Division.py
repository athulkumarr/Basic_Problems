def divide(self, dividend: int, divisor: int) -> int:
	temp = 0
	quotient = 0

	# Determining the sign of the quotient 
	sign = (-1 if ((dividend < 0) ^ (divisor > 0)) else 1)
	
	dividend = abs(dividend)
	divisor = abs(divisor)
	
	# -2^31 <= dividend, divisor <= 2^31 -1
	for i in range(31, -1, -1):
		
		if (temp + (divisor << i) <= dividend):
			temp += divisor << i
			quotient |= 1 << i
	
	#if the sign value computed earlier is -1 then negate the value of quotient
	if sign == -1:
		quotient = -quotient

	return quotient

print(divide(10,3))
