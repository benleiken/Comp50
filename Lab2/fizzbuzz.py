#FizzBuzz
#Prints numbers 1-100. If # is multiple of 3 prints Fizz, if multiple of 5 prints Buzz
i = 1	
while( i< 100):
	if( (i % 3) == 0 and (i % 5) == 0):
		print("FizzBuzz")
	elif( (i % 3) == 0):
		print("Fizz")
	elif( (i % 5) == 0):
		print("Buzz")
	else:
		print(i)
	i += 1