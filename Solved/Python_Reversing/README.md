# Python Reversing
Reverse Engineering - 40 points

## Challenge 

Written by jfrucht25

Found this flag checking file and it is quite vulnerable

[Source](3e4bb82e4f30d27f9ba62d1c7885e448b5442448c5e00c58fd28de9cf17cd364_source.py)

## Solution

#### Understanding the encryption

Let's tackle the challenge by reversing it...

- the flag is converted to a list of ASCII codes in `arr`
- numpy random is seeded to `12345` & generated integers in the variable `other`
- the random numbers and the flag ASCII codes are multiplied respectively
- XOR cipher is used on the flag with key of `ligma_sugma_sugondese_`
- The final ciphertext is converted to binary string.

---

I tried to do it in reverse, but then I found out that after multiplying the flag with the numpy random array, it could mean that the char value is now more than 8 bits.

Assuming 7-bit ASCII,
- If multiply by 1 or 2, result is within 8-bits (2 hex chars).
- If multiply by 3 to 5, result is variable from 8-bits to 12-bits (2 to 3 hex chars)

Also, note that the XOR cipher is done after multiplication.

---

#### More efficient solution

While a good solution is to collectively examine the bits until a valid char is produced, a faster way will be to bruteforce the input and compare to the output.

	Python_Reversing $ python3 solve.py 
	Progress: tjc
	Progress: tjct
	Progress: tjctf
	Progress: tjctf{
	Progress: tjctf{p
	Progress: tjctf{pY
	Progress: tjctf{pYt
	Progress: tjctf{pYth
	Progress: tjctf{pYth0
	Progress: tjctf{pYth0n
	Progress: tjctf{pYth0n_
	Progress: tjctf{pYth0n_1
	Progress: tjctf{pYth0n_1s
	Progress: tjctf{pYth0n_1s_
	Progress: tjctf{pYth0n_1s_t
	Progress: tjctf{pYth0n_1s_tr
	Progress: tjctf{pYth0n_1s_tr1
	Progress: tjctf{pYth0n_1s_tr1v
	Progress: tjctf{pYth0n_1s_tr1v1
	Progress: tjctf{pYth0n_1s_tr1v14
	Progress: tjctf{pYth0n_1s_tr1v14l
	Progress: tjctf{pYth0n_1s_tr1v14l}

## Flag

	tjctf{pYth0n_1s_tr1v14l}
