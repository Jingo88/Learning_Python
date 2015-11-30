# # List

# def fibo(n):
# 	x = 1
# 	y = 1
# 	my_numbers = []
	
# 	for n in range(n):
# 		my_numbers.append(x)
# 		x = y
# 		y = x + y
# 	return my_numbers

# print(fibo(10))

# # Generator
def fibo(n):
    x = 1
    y = 1

    for n in range(n):
        yield x
        x = y
        y = x + y

for num in fibo(10):
    print(num)
