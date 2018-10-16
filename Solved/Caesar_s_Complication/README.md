# Caesar's Complication
Cryptography - 20 points

## Challenge 

Written by evanyeyeye

King Julius Caesar was infamous for his [wordsearch](735e2c6249eafe7f70c396fe4e808c1ce4a3c073238b66286fa0d59a6fd4b88c_puzzle) solving speed.

## Solution

Since this is a word search, I decided to make some functions to search horizontal, vertical and diagonal.

Also knowing this is a caesar cipher, I made an array of regex search keys for ROT0 to ROT25

	$ python3 solve.py 
	Horizontal
	[]

	Vertical
	[]

	Diagonal Left
	[]

	Diagonal Right
	[]

However, after doing so, there's no results.

Word searches also may contain reversed words, so I made another array with reversed of the regex

	$ python3 solve.py 
	Horizontal
	[]

	Horizontal Reversed
	[]

	Vertical
	[]

	Vertical Reversed
	[]

	Diagonal Left
	[]

	Diagonal Left Reversed
	[]

	Diagonal Right
	[]

	Diagonal Right Reversed
	['}alwtys}wli}zujsexgkwva{xlubl']

Now, we found something. Reverse it and we get this at ROT8

	ROT0	'lbulx{avwkgxesjuz}ilw}sytwla}'
	ROT8	'tjctf{idesofmarch}qte}agbeti}'

Fun challenge indeed!

## Flag

	tjctf{idesofmarch}
