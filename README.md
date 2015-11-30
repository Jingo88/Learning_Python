# Learning Python
---

## Chapters

##### [I. Data Types](#datatypes)
##### [II. Data Structures](#datastructures)
##### [III. Control Flow and Statements](#controlstatements)
##### [IV. Errors and Exceptions](#errors)
##### [V. Built In Functions](#builtin)
##### [VI. Python OOP](#oop)


### Terminal Trick

* You can type `variablename.` with the period at the end, and it will give you all the methods that can be used on that variable
* Ipython - a better version of terminal python. (like irb vs pry?)
* pdb and ipdb - this is the debugging tool

### Variable Declaration
* Does not require `var`
* Variables are written in snake case 
* Cannot start with number
* Cannot declare with special case
* Commenting Symboles
	* `#` = One Line
	* """ some comment """ = multiple lines

### Indexing

* Indexing in strings and lists are the same. We have this cool shit now with using colons
	* `x[:3]` gives us the values of all the indexes from zero UP TO BUT NOT INCLUDING three
	* `x[:]` grab everything
	* `x[-1]` grab the last letter or value
	* `x[:-1]` grab everything but the last letter or value
	* `x[::2]` grab every other letter or value
	* `x[::-1]` reverse a string or list

### <a name=datatypes>Data Types</a>

***Numbers***

* Integers: whole number `7`
* Floats: decimal number `7.00`
* Math is all the same as JS
	* `+`, `-`, `*`, `/`, `**`, `%`
	* add, subtract, multiply, divide, exponent, modulo
* Division in Python 2 vs Python 3
	* `/` in P2 gives us classic division. `3/2 == 1` and `3.0/2 == 1.5`
	* `/` in P3 gives us true division. `3/2 == 1.5`
		* Python 3 kind of eliminates floats (7/2 == 3 || 7/2 == 3.5)
* `!=`, `==`
	* No threequals 
* `0`, `""`, `null` are `false`, and everything else is `true` 

***Strings***

* Strings are immutable. Once it is created, you cannot change it. You can concatenate them, to add things to it, but you cannot change the existing elements. 
* print in Python 2 `print "hello world"`
* print in Python 3 `print("hello world")`
	* print is a function in Python 3 	
* The `\` symbol is still escape from strings
	* `\t` will tab
* String concatenation 
	* `+` 
	* With Variables: `"%s" % (varOne, varTwo)` then use the % to input the variable into the string. `%s` says convert to string
	* With Floats: `%1.2` - the first number is the minimum number of digits the variable should have, the second number is how many digits to show after the decimal 
	* With Variables: `{}` and the `.format()` method

```
varOne = "Jason"
varTwo = "Instructor"
x = 10.5732

print "My name is %s, and I am an %s." % (varOne, varTwo)
print "My number is %1.2f" %(x) == 10.57
OR

print "My name is {}, and I am an {}".format(varOne, varTwo)
print "format is {x}, it makes is type less. That is {x}".format(x=great)
```

---
### <a name=datastructures>Data Structures</a>

***Lists***

* Lists are like arrays
	* `["I", "am", "an", "array"]`
* Mutable, unlimited, uses methods and shit 
* List Comprehension - deconstructing a for loop within a bracket to create an array. Make a list of dynamic values with one line of code
	* `[row[0] for row in rows]`
	* For every element in the rows grab the first index and return an array of all the first index values

```
[expression for/in loop if conditional]

[x**2 for x in range(10) if x>3]

// [16,25,36,49,64,81]
```
* You can call on this list like a regular list

```
large_squares = [x**2 for x in range(10) if x>3]
large_squares[1]
```
* The if conditional is optional

```
[x**2 for x in range(10)] == [1, 4, 9, 16, 25, 36, 49, 64, 81]
```
***Dictionaries***

* Dictionaries `{}` = where we store key:value pairs
	* No indexing, uses key mapping instead.
	* Keys are usually written as strings
	* We call the values the same way as JS and Ruby `dictionaryName[key]`


***Tuples***

* Tuples `()`= an immutable array
	* Indexing same as strings and lists
	* Use to ensure certain data stays the same forever
	* runs faster than lists
	* `("This", "cannot", "change")`
	
***Sets***

* Sets are written with curly braces and are unordered collections that only contain unique elements

```
my_list = [1,1,1,2,3,3,3,3,4,5,5,5,6,6]

my_set = set(my_list) // {1,2,3,4,5,6}
```

---
### <a name=controlstatements>Control Flow & Statements</a>
* Comparators all the same shit
	* `==`, `!=`, `<=`, `>=`, `<`, `>`
* Chaining Operators

	```
	1 < 2 < 3
	//is 1 less than two AND is two less than three
	```
* Boolean Operators are written as 
	* `and` - evaluated next
	* `or` - evaluated last
	* `not` - evaluated first

***White Spacing***

* Indented code uses four spaces
* Use to separate statements

```
def first_one():
    if 2==2:
        return "You are #1"

def second_one():
    if 5>3:
        return "You are still NUMBER ONE"

print first_one()
print second_one()
```

***If/Else Statementes***

```
def sum_hundred(answer):
    if answer > 100:
        return 1
    elif answer < 100:          
        return -1
    else:
        return 0
        
print sum_hundred(90)
print sum_hundred(110)
print sum_hundred(100)
```

***For Loops***

* For In Loop

```
numbers = [1,2,3,4,5]

for num in numbers:
	print(num)
```

* Tuple Unpacking - if you have tuples in a list you can target the values in the tuples using the for in loop

```
my_list = [(1,3), (5,7), (9,11)]

for (t1, t2) in my_list:
	print t1
```

* Dictionary - For in loops in Python allow us to target both the key and the value

```
d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
	print k
	print v
```
* In Python 2 you will use `d.iteritems()` instead of `d.items()`

***While Loop***

```
x = 0

while x < 5:
	print "the number is " + x
	x += 1
```
* Break: Breaks out of the current closest enclosing loop 
* Continue: Goes to the top of the closest enclosing loop
* Pass: Does nothing

```
x = 0

while x < 20:
	print "the number is ", x
	print "Incrementing the number until it is 20"
	x += 1
	
	if x == 5:
		print 'The number is now five!'
	elif x == 10:
		print "hey it's now ten"
		break
	else:
		print "going to keep going"
		continue
```

***range()***

* returns a list of values
* Some syntax
	* range(stop)
	* range(start, stop[, step])

```
range(0,5) // [0, 1, 2, 3, 4]

range(5,10) // [5, 6, 7, 8, 9]

range(0, 10, 2) // [0, 2, 4, 6, 8]
```
* `Python 2` has a built in generator called `xrange()`
	* Use this if you wanted to loop through a generated list but not have that list stored to memory
* `Python 3` - the `range()` method is already a generator. No need for `xrange()`

***List Comprehension***

* You are creating a list by flattening out a for loop
* [Expression / For Loop / Condition]

```
- A list of each letter as a value
[letter for letter in 'hello'] // ['h', 'e', 'l', 'l' , 'o']

- A list that will multiply every value by two and store them
[x*2 for x in range(0,5)] // [0, 2, 4, 6, 8]

- A list that will have a condition
- Give me even numbers
[num for num in range(5, 11) if num % 2 == 0] // [6, 8, 10]

- Nested List Comprehension
- double the above multiplication list
double = [x*2 for x in [x*2 for x in range(0,5)]] // [0, 4, 8, 12, 16]
```

***Lambdas***

* Lambda - a one line version of a function
* Syntax
	* `lambda name_of_element: Expression`
	
```
double = lambda num: num*2
double(25) 
// 50
```
* [Python Conquers the Universe](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)
	* Taken from the above blog post
		* "The most common use for lambda is to create anonymous procedures for use in GUI callbacks. In those use cases, we don’t care about what the lambda returns, we care about what it does."	
* We don't "NEED" lambdas. But it helps to make cleaner code
* Used for simple functions that does one expression
* Similar to a short anonymous function. Lambdas are usually not saved
	* More like anonymous procedures rather than anonymous functions
* Used a lot with `map()`, `filter()`, `reduce()`
* Also used frequently to declare "callback" functionality
* We do not have to explicitly call `return`
	* Since we only have one expression, and that expression should return a value, lambdas have `implicit returns`

```
def sum(x,y): return x + y
	
sum = lambda x,y: x+y
```


---
### <a name=errors>Errors and Exceptions</a>

* Exceptions - a specific type of error
	
***Try and Except Statement***

* Try - where you do your operation
* Except - If a specific `Exception Error` occurs do something else
* Else - if there is no exception run the block of code
* Finally - code that will always run even if there is an exception

```
try:
	10 + "Hello"
except TypeError: 
	print "You have a type error, cannot add two different data types"
finally:
	print "You printed something..."
```
* You can also put it in a method
* The exception will only check a second time once

```
def ensure_integer():
			
	try: 
		val = int(input("Enter a number"))
	except:
		print("You did not enter a number"				val = int(input("Make sure you only entered numbers, no other characters"	finally: 
		print("This block of code has finised")
	print(val)
```
* Using a loop to make sure the user eventually enters a number

```
def ensure_integer():
			
	while True		
		try: 
			val = int(input("Enter a number")
		except:
			print("You did not enter a number"	
			continue
		else: 
			print("We have a number!")
			break
		finally: 
			print("This block of code has finised")
		print(val)
```



* The try should be as small as possible. It will only be the part that has the capacity to fail
* except - name of the error. 

```
try:
	5/0
except ZeroDivisionError:
	print("Cannot Divide by zero.")
else:
	print("That is Impossible")
```
* ZeroDivisionError is a type of exception
* You can do a catch all exception but this won't be specific

```
try:
	5/0
except Exception:
	print("Cool beans homie")
else:
	print("That is Impossible")
```
* You can also do multiple `excepts` in multiple lines or on the same line

```
try: 
	5/0
except ValueError:
	print("You got value error")
except ZeroDivisionError:
	print("You got zero division")
else:
	print("All good in the hood")


try: 
	5/0
except ValueError, ZeroDivisionError:
	print("You got one of these two errors")
else:
	print("All good in the hood")
```

### <a name=builtin>Built In Functions</a>

***These are called functions because methods are "Functions inside of a class"***

***map()***

* Takes two arguments, a function and a sequence. 
* It will apply that function to every element within the sequence that was passed in

```
my_nums[5, 7, 23, 14, 2, 9, 58]

def two_times(x):
	return x*2

double = map(two_times, my_nums)
```
* Lambdas can also be useful instead of defining specific functions

```
map(lambda num: num*2, my_nums)
```
* More Lambda stuff

```
my_nums = [10, 15, 20]
your_nums = [2, 4, 6]

map(lambda num1, num2: num1*num2, my_nums,your_nums)

//You could even add a third if you wanted

map(lambda num1, num2, num3: (num1*num2)/num3, my_nums,your_nums,another_nums)
```

***reduce()***

***This was removed from the built-in functions in Python2 and is in `functools` of Python3***

***Below is the syntax for reduce() in Python2***

* Takes two arguments, a function and a sequence.
* You will continue to "reduce" the sequence until a single value is left
* You will be applying the function to the first two elements, then the result of that function with the third element, then the result with the fourth element, so on and so forth. 

```
my_num = [5, 23, 14, 28, 90, 49]
def greater_num(a, b):
	if a > b:
		return a
	else
		return b

max_num = reduce(greater_num, my_num)
// Compares 5 > 23, return 23
// Compares 23 > 14, return 23
// Compares 23 > 28, return 28
// Compares 28 > 90, return 90
// Compares 90 > 49, return 90
// max_num == 90
```
* Another example

```
num_list = [1, 2, 5, 10, 12, 15]

all_sum = reduce(lambda x,y: x+y, num_list)
```

***filter()***

* Takes a function and a list as an argument
* The function will continue to run and return a Boolean Value. If it returns True on that element, that element will be included in the result
* You're filtering shit out

```
filter(lambda num: num%2 == 0, my_num)
//Will return a list with all the even values from my_num
```

***zip()***

* Zip allows us to iterate through two separate data structures and will merge them together as tuples in a list
* Zip will take the shortest of the data structures

```
a = [1, 3, 5]
b = [2, 4, 6, 23, 14, 25]

zip(a, b) 
// [(1, 2), (3, 4), (5, 6)]
```
* Dictionaries will only target the keys when iterating. 
* Use `itervalues()` to target their values

```
mine = {'a':1,'b':2}
yours = {'c':4,'d':5}

zip(mine,yours)
//[('a', 'c'), ('b', 'd')]
```

***enumerate()***

* Takes two arguments, a count and an element
* Keeps a count as you iterate through an object

```
vowels = ['a','e', 'i', 'o','u']

for count, item in enumerate(vowels):
	print count
	print item
//0
//a
//1
//e
// so on and so forth
```
* the `count` above is just the iterator, so you can name it "i" or "n"

***all() and any()***

* all - returns true if all elements in the iterable are true
* any - returns true if any of the elements in the iterable are true 

```
my_booleans = [True, False, True, False, False, False]

all(my_booleans) // False

any(my_booleans) // True
```

***Complex()***

* Takes care of complex numbers
* Can take numbers or strings
* Some math shit you should look into
* 

```
complex(2, 3)
//(2 + 3j)

complex(10, 1)
//(10 + 1j)

complex("10 + 2j")
//(10 + 2j)
```


***MOAR FUNCTIONS!!!***

* `len()` - what is the length of variable
* `lower()` - string to lowercase
* `upper()` - string to uppercase
* `str()` - convert variable to string
* `split()` - returns a string as a list, and splits the string into list values at the requested point. 
* `pop()` - remove the last value in an array
* `reverse()` - reverse a array
* `items()` - use on a dictionary. returns the keys and values as tuples in a list
* `print()` - print to console
* `input()` - get input from user through console
* `type()` - type of variable
* `append()` - put a value in a list, last index
* `insert()` - put a value in a list, first index
* `range()` - returns a list with values from zero to the number in the range. Can also take two parameters
* `index()` - what is the index of a certain value
* `count()` - how many times a value appears
* `next()` - `yield` (not return) the next value in a list
* `iter()` - print every letter in a string/list

***Built In Functions For Math and CS Shit***

* `hex()`
* `bin()`
* `pow()`
* `abs()`
* `round()`

---
### Files

* `open('filename')` - open a file to your code
* `variable.read()` - read a file in your code 
	* if you use the `read()` method again it won't return anything. This is because python has the "cursor" at the end of the file and you have to bring it back to the top of the file to read
* `seek(0)` - start at the beginning of the file

```
f = open('my_file.txt')

f.read() 				//reads the text

f.seek(0) 				//goes back to beginning of file
```
* `readlines()` - goes through every line in the file and returns a list, each line is it's own value. 
	* this stores items in memory so be careful, using readlines for a giant book may take forever
	
---
### Generators

* [Stack Overflow Generators](http://stackoverflow.com/questions/1756096/understanding-generators-in-python)
* [Stack Overflow Iterators](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
* [Blog Post About Yield](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)
* Allows the generation of objects that are provided in that instance but not stored in memory. 
	* Example: You want to use `range` to create a large list to loop through but do not need that list to be stored anywhere
* `Yield` using the yield keyword will make a function turn into a generator. 
	
***TWO EXAMPLES***

* (NOT GENERATOR)Storing a list in memory. This can be a hassle if you put in a big number

```
def double(num):
	a = 1
	
	my_nums = []
	
	for i in range(num):
		a = a*2
		my_nums.append(a)
	
	return my_nums	

double(5)
//[2, 4, 8, 16, 32]
```
* (GENERATOR)It will only store the value at that moment in time. Lets pass in a list and double every value

```
def double(x):	
	for num in range(x):
		yield num*2

for x in double(10):
	print(x)
//0
//2
//4
//6
//8
//etc
```

***FIBONACCI***

* Because you have to know how to do this in every freakin language...........

```
def fibo(n):
	x = 1
	y = 1

	for n in range(n):
		yield x
		x = y
		y = x + y

for num in fibo(10):
	print(num)
```




---
### Scope

* Scope - the same shit as Ruby and JS. Keep it OOP!
	* Local - Variables declared in a function
	* Enclosing Functions - Variables declared in local scope of nested functions. Inner to Outer. (Same as lexical scoping in JavaScript)
	* Global - Global Shit
	* Built-In - Variables preassigned in the built in names module
* You can use `globals()` and `locals()` method to check the status of a variable
	
### <a name=oop>Python OOP</a>

* Everything in Python is an object

***Classes***

* Class name are capitalized
* Always use `self` in the `__init__()` method
	* like initialize in ruby. self is like "this"
	* You can also set defaults to attributes in the init method just like in Ruby
* `Class Object Attributes` - like class variables in ruby
	
```
class Car(object):
	type = "vehicle"
	wheels = 4

	def __init__(self, brand, model, headlights=True): 
		self.brand = brand
		self.model = model
		self.headlights = headlights

jasons_car = Car(brand = 'Bugatti', model = 'Veyron')
```

***Methods***

* Defined functions inside a class
* Call self on these methods just like the `__init__()`
* Use the Car example above

```
class Car(object):
	type = "vehicle"
	wheels = 4

	def __init__(self, brand, model, headlights=True): 
		self.brand = brand
		self.model = model
		self.headlights = headlights
		
	def travel(self, dest):
		print("You are traveling to " + dest)

jasons_car = Car(brand = 'Bugatti', model = 'Veyron')
jasons_car.travel("New York")
```

***Inheritance***

* You can inherit the properties of another class just like in Ruby. 
* You call the superclass in the parenthesis after the class name
* The below example is if the `Car` class inherited from a `Vehicle` class

```
class Vehicle(object):
	def __init__(self):
		print("You have a new vehicle")
		
class Car(Vehicle):
	def __init__(self):
		Vehicle.__init__(self)
		print("It's a Car!")
		
new_car = Car()
// You have a new vehicle
// It's a Car!
```

***Special Methods***

* Special methods are shown with the double underscores
* `string`, `length`, `delete`

```
class Car(object):
	type = "vehicle"
	wheels = 4

	def __init__(self, brand, model, headlights=True): 
		self.brand = brand
		self.model = model
		self.headlights = headlights
	
	def __str__(self):
		return "Your car is a %s %s" %(self.brand, self.model)

	def __len__(self):
		return self.brand
	
	def __del__(self):
		return "You wrecked your car!!!"
		
jasons_car = Car(brand = 'Bugatti', model = 'Veyron')
str(jasons_car) // "Your car is a Bugatti Veyron"
len(jasons_car)
del(jasons_car)
```

### Modules

* There are some modules that come with Python. Import them to use their functions. Same as requiring gems or npm packages

```
import math //you import the whole thing

OR 

from math import sqrt //you import a specific thing
```
* Install modules not built in using Terminal
	* Make sure to google some shit first and check out the docs, as usual

```
pip install module_name
```

***Collections***

* Provides us with:
* `counter()` - counts the num of occurencies in an object. returns a has with the initial objects values as keys, and their occurencies as values
* `defaultdict()` - Allows us to set a default value to new keys in a dictionary. Will never raise a KeyError. 

```
d = defaultdict(lambda: 0)
d['a'] // 0
d['b'] = 50 // 50
```

* `OrderedDict()` - Remembers the order which content was added to an object. This can be helpful because dictionaries don't normally retain an order, they are just mapping shit for you. 

```
dict_a = {}
dict_a['x'] = 80
dict_a['y'] = 50

dict_b = {}
dict_b['x'] = 50
dict_b['y'] = 80

dict_a == dict_b // Will return True

BUT

dict_a = OrderedDict()
dict_a['x'] = 80
dict_a['y'] = 50

dict_b = OrderedDict()
dict_b['x'] = 50
dict_b['y'] = 80

dict_a == dict_b // Will return False
```

* `namedtuple()` -  Acts as a normal tuple, however it creates a new object type and allows users to declare various fields
	* var_name = namedtuple("object name", "various fields")
	
```
Car = namedtuple("Car", "brand model year")

jasons_car = Car(brand="Bugatti", model="Veyron", year="2013")

jasons_car.model == "Veyron"
```

***Datetime***

* A module that deals with timestamps in your code. Use this shit a bunch in Django tutorials
* Some syntax for `datetime.time`
	* the_time = datetime.time(hour, minutes, seconds, microseconds(ms is optional))
	* You also have access to `min()`, `max()`, `resolution()`
	
```
my_time = datetime.time(2, 0, 0)

// 02:00:00
```
* Some syntax for `datetime.date`
	* the_day = datetime.date(year, month, day)
	* Also have access to `timetuple()`, `year()`, `month()`, `day()`, `min()`, `max()`, `today()`

```
birthday = datetime.date(2015, 10, 29)
// 2015-11-29
```
* Calculating the difference between two dates

```
import datetime

first_date = datetime.date(2005, 2, 26)
today = datetime.date.today()

print(first_date)
print(today)

print(first_date - today) #-3928 days, 0:00:00
print(today - first_date) #3928 days, 0:00:00
```

***timeit***

* Used to time parts of your code to see how long it takes. Helps to see if some code is slowing things down
* Syntax = timeit.timeit('pass your expression to test as a string', the number of times you want it to run)

```
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

//0.2342234581739372 <--something like that
```
* You can use the `%` to break down stats further

```
%timeit "-".join(str(n) for n in range(100))

// 10000 loops, best of 3: 23.8 µs per loop
```

***REGEX***

* `import re`
* We can search for patterns in text
	* Syntax == `re.search(pattern, text)`

```
re.search("name", "My name is Jason")
// Returns a "Match" object
``` 
* If there was no match it would return "None"
* Look at your old REGEX lecture notes

***StringIO***

* Convert strings into file like objects
* we can then read and write to these objects as if they were files

***Python Debugger PDB***

* similar to pry or debugger. Some syntax differences
* use `pdb.set_trace()` to pause the code at that moment in time and browse around
* press `q` to quit

```
import pdb

a = "Hello World"
b = [1,2,3]

pdb.set_trace()

print(a + b)
```

### Decorators

* Try this blog post [http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
* Objects can be assigned to a function, and still work, even if that function gets deleted

```
def func_a():
	print "blah"

var_b = func_a

del func_a

var_b() // "blah"
```
* Functions that modify what other functions do
* Using functions within functions or passing functions as arguments to other functions
* Not invoking items immediately but assigning it to a variable using another function. (Remember, using parenthesis invokes functions immediately)

```
def great_hundred(x):
	
	def correct():
		return "Your number is greater than 100"
	
	if x > 100:
		return correct
		
my_num = great_hundred(200) 
//my_num = correct
```
* Longer Example for passing functions as arguments

```
def new_decorator(func):

    def wrap_func():
        print "Code would be here, before executing the func"

        func()

        print "Code here will execute after the func()"

    return wrap_func

def func_needs_decorator():
    print "This function is in need of a Decorator"
```
* Now we can reassign the second function to pass it into the first

```
func_needs_decorator = new_decorator(func_needs_decorator)
```
* Using decorators we can re-write this to look like:

```
@new_decorator
def func_needs_decorator():
    print "This function is in need of a Decorator"
```