###########################################################################################
# Pass in a number. 
# Print out the fibonacci sequence up to that number
# The sequence will start at "1" and continue to add the next value to the sum of the previous two values
# [0,1,2,3,5,8,13,21,34]
###########################################################################################

import pdb


# The below functions don't give me the proper output, it's giving me:
# [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
# fix that shit when you get home

# # List
def fibo(n):
	x = 0
	y = 1
	my_numbers = []
	
	for n in range(n):
		my_numbers.append(x)
		x = y
		y = x + y
		# pdb.set_trace()
	return my_numbers

print(fibo(10))

# # Generator
# def fibo(n):
#     x = 0
#     y = 1

#     for n in range(n):
#         yield x
#         x = y
#         y = x + y

# for num in fibo(10):
#     print(num)
