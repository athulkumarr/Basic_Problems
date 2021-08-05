def russianPeasant(a, b):
 
	# initialize product
    product = 0 
 
    # While second number doesn't become 1
    while (b > 0):
     
        # If second number becomes odd, add the first number to result
        if (b & 1):
            product += a
 
        # Double the first number and halve the second number
        a = a << 1
        b = b >> 1
     
    return product
