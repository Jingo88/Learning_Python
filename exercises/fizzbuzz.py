###########################################################################################
# Pass in a number. 
# If the number is divisible by 3 print the word "Fizz".
# If the number is divisible by 5 print the word "Buzz".
# If the number is divisible by 3 and 5 print the word "FizzBuzz"
###########################################################################################


# def fizzbuzz(n):
# 	for n in range(n):
# 		if n%3==0 and n%5==0:
# 			print("FizzBuzz")
# 		elif n%3 == 0:
# 			print("Fizz")
# 		elif n%5 == 0:
# 			print("Buzz")
# 		else:
# 			print(n)

# fizzbuzz(25)

# If you want to check one number just remove the for loop

def fizzbuzz(n):
	if n%3==0 and n%5==0:
		print("FizzBuzz")
	elif n%3 == 0:
		print("Fizz")
	elif n%5 == 0:
		print("Buzz")
	else:
		print(n)

fizzbuzz(15)