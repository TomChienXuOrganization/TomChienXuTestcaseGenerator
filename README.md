# CP Testcase Generator
A comprehensive test generator (exclusively designed for administrators). You do have the correct solution, then this will do everything remains for you!

- You're creating a problem for your contest?
- You have already had the statements and solutions but don't want to generate testcases by yourself?
Then you're in the right place! We will help you to resolve that issue!

## How to use it?
To be honest, it's fairly simple! You just have to install **Python** (any version **above 3.7** or **3.7** itself), then download or clone our **Github Repository**.
To use it, you must have a correct solution of the problem.

1. First, import the `TestGenerator` class in `generator.py` file:

```
import generator
# or
from generator import TestGenerator
# Please put the generator.py file in the same folder
```

2. Now we'll setup a custom `TestGenerator`:
- In the `TestGenerator` class, there are $4$ main functions, they are:
    - `__init__`: Of course, every class consists of that function. It takes $3$ **OPTIONAL** arguments which are:
	    -  `name` (default value is `"default"`)
	    - `number_of_testcases` (default is `10`)
	    - `syntax` (which means IO-Syntax, default is `["input.%0_id_3%", "output.%0_id_3%"]`)
    - `algorithm`: An abstract method, it takes $1$  argument that is `input_`.
    - `set_input`: An abstract method, it takes $1$  argument that is `index`.
    - `generate`: It's our thing :)
  
- Ok, now we'll have to setup our custom class:
```
# Name the class anything you want :D
# But it must be a subclass of generator.TestGenerator.

class ConCuLeLe(TestGenerator):

	# If you prefer our default properties;
	# then you don't have to define the __init__ function.

	# If you keep one (or more) of our default properties;
	# just keep what to be edited in the super().__init__() function.
	def __init__(self) -> None:
	
		super().__init__(
			name="cai gi do",
			number_of_testcases=69420,
			syntax=["%1_id_1%.in", "%1_id_1%.out"]
		)
```

Maybe a lot of creepy dudes online will wonder `What the f*ck in the world is IO-Syntax?`, then:
-   IO-Syntax (Input/Output Syntax) is the way the online judger recognize how to access the input and output files while doing the judging process.
-   Basically, these are name-patterns of the input and output files which you zip in a compressed file.
-   You can put anything you want, but they must consist of a number pattern like this  `%(number_1)_id_(number_2)%`. In which:

	-   `(number_1)`  is the start number of the testcases. Case in point, if your set of tests starts with number  `0`  then  `(number_1)`  should be  `0`. Otherwise, if it starts with  `1`  then  `(number_1)`  would be  `1`.

	-   `(number_2)`  is the minimum number of digits. For example, if the test number is  `000`, in that case your  `(number_2)`  should be  `3`. Even if the number is  `55555`, the  `(number_2)`  still does its job great!

-   **Real time examples:**

	-   If you're using  [LuyenCode](https://oj.luyencode.net/)'s judging testcases (like  `1.in`  and  `1.out`,...), they start with  `1`  and their minimum number of digits is  `1`. Due to that, the input syntax is  `%1_id_1%.in`  and the output syntax is  `%1_id_1%.out`.
	-   Second example, if you're using something like  `input.000`,  `output.000`  and so on, they start with  `0`  and their minimum number of digits is  `3`. Due to that, the input syntax is  `input.%0_id_3%`  and the output syntax is  `output.%0_id_3%`.

Hmmm, that's gud! Now we have to define the `algorithm` function:

```
class ConCuLeLe(TestGenerator):

	# This function contains the way(s) it will solve the problem.
	# It will be granted 1 argument, which is the input (a string).
	# It must return a string (result of the problem with that input line).
	# By the way, you musn't print the result, instead, return them!
		
	def algorithm(self, input_: str) -> str:
		...
	
	# For example, this is a simple algorithm for Sum of 2 integers problem!
	
	def algorithm(self, input_: str) -> str:
		return sum(map(int, input_.split()))
		# or 
		a, b = [int(i) for i in input_.split()]
		return a + b
		# what ever you can think of, just replace print with return.
```

Ma boi, nearly done! Set input with the `set_input` method:

```
class ConCuLeLe(TestGenerator):

	# This function provides the input for the algorithm method!
	# @ These 2 methods must fit each other!
	# It will be granted 1 argument (just an index number not that necessary).
	# (This number will take it position when you need to generate test
	# for multiple testcase-scores and limiations)
	# It must return a string (input for algorithm method).
		
	def set_input(self, index: int) -> str:
		...
	
	# For example, this is a input for Sum of 2 integers problem!
	
	from random import randint as a
	def set_input(self, index: int) -> str:
		return f"{a(10**8, 10**9)} {a(10**8, 10**9)}"
		
	# It will return something like: "69696969 69696969"
	# and it fits perfectly with algorithm method!
```
We're done!!! Now to generate, write this final line:

```
ConCuLeLe().generate()
```

The final testcases will be in `problems/{name}/testcases`! Have fun :D
