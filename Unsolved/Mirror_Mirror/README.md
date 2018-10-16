# Mirror Mirror
Miscellaneous - 100 points

## Challenge 

Written by Alaska47

If you look closely, you can see a reflection.

`nc problem1.tjctf.org 8004`

## Solution

	$ nc problem1.tjctf.org 8004
	Hi! Are you looking for the flag? Try get_flag() for free flags. Remember, wrap your input in double quotes. Good luck!

	>>> get_flag()
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	TypeError: get_flag() takes exactly 1 argument (0 given)

	>>> dir()
	['__builtins__', '__doc__', '__name__', 'get_flag']

	>>> __version__
	Sorry, that's not allowed.

Trying out

	Hi! Are you looking for the flag? Try get_flag() for free flags. Remember, wrap your input in double quotes. Good luck!
	>>> 
	>>> get_flag("!")  
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	  File "/home/app/problem.py", line 23, in get_flag
	    if(eval(input) == super_secret_string):
	  File "<string>", line 1
	    !
	    ^
	SyntaxError: unexpected EOF while parsing

https://lbarman.ch/blog/pyjail/

	>>> dir(get_flag)
	['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
	>>> get_flag.func_code 
	<code object get_flag at 0x7f8574f004b0, file "/home/app/problem.py", line 15>
	>>> get_flag.func_code.co_consts
	(None, 'this_is_the_super_secret_string', 48, 57, 65, 90, 97, 122, 44, 95, ' is not a valid character', '%\xcb', "You didn't guess the value of my super_secret_string")


https://akaptur.com/blog/2013/11/15/introduction-to-the-python-interpreter-2/

	>>> dir(get_flag.func_code)
	['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
	>>> get_flag.func_code.co_filename
	Sorry, that's not allowed.
	>>> get_flag.func_code.co_name
	'get_flag'
	>>> get_flag.func_code.co_varnames
	('input', 'super_secret_string', 'each', 'val')



## Flag

	??