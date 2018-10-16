# Bad Cipher
Reverse Engineering - 50 points

## Challenge 

Written by nthistle

My friend insisted on using his own cipher program to encrypt this flag, but I don't think it's very secure. Unfortunately, he is quite good at Code Golf, and it seems like he tried to make the program as short (and confusing!) as possible before he sent it.

I don't know the key length, but I do know that the only thing in the plaintext is a flag. Can you break his cipher for me?

[Encryption Program](daeb831c7db4609d7684c49b6bb54bbb1ea20a0870543debee80d13eb84e5370_bad_cipher.py)

[Encrypted Flag](e71609ba3434b0e34d3f16966f1ab1c321f4f81e62593e6b8c9cb835fcb5906f_flag.enc)

## Solution

#### Reverse the encoder (decoding)

Upon debugging the encoder, I noticed that with a plaintext of 'hello world' and key of 'abc', some chars are missing from the final ciphertext

	$ python3 original.py
	['hlwl', 'eood', 'l r']
	h 0x68 ^ 0x61 ^ 0x0 = 0x9
	l 0x6c ^ 0x61 ^ 0x2 = 0xf
	w 0x77 ^ 0x61 ^ 0x3 = 0x15
	l 0x6c ^ 0x61 ^ 0x5 = 0x8
	e 0x65 ^ 0x62 ^ 0x0 = 0x7
	o 0x6f ^ 0x62 ^ 0x1 = 0xc
	o 0x6f ^ 0x62 ^ 0x3 = 0xe
	d 0x64 ^ 0x62 ^ 0x3 = 0x5
	l 0x6c ^ 0x63 ^ 0x0 = 0xf
	  0x20 ^ 0x63 ^ 0x3 = 0x40
	r 0x72 ^ 0x63 ^ 0x10 = 0x1
	['\t\x0f\x15\x08', '\x07\x0c\x0e\x05', '\x0f@\x01']
	
	09070f0f0c40150e01
	['\t\x0f\x15', '\x07\x0c\x0e', '\x0f@\x01']

It seems that for it to decode properly, the plaintext ***must be a multiple of the key length.***

With this, I successfully made a decode function which works

	$ python3 debug.py
	------------------------------
	Encode:
	['hlwl', 'eood', 'l r!']
	h 0x68 ^ 0x61 ^ 0x0 = 0x9
	l 0x6c ^ 0x61 ^ 0x2 = 0xf
	w 0x77 ^ 0x61 ^ 0x3 = 0x15
	l 0x6c ^ 0x61 ^ 0x5 = 0x8
	e 0x65 ^ 0x62 ^ 0x0 = 0x7
	o 0x6f ^ 0x62 ^ 0x1 = 0xc
	o 0x6f ^ 0x62 ^ 0x3 = 0xe
	d 0x64 ^ 0x62 ^ 0x3 = 0x5
	l 0x6c ^ 0x63 ^ 0x0 = 0xf
	  0x20 ^ 0x63 ^ 0x3 = 0x40
	r 0x72 ^ 0x63 ^ 0x10 = 0x1
	! 0x21 ^ 0x63 ^ 0x0 = 0x42
	['\t\x0f\x15\x08', '\x07\x0c\x0e\x05', '\x0f@\x01B']
	09070f0f0c40150e01080542
	------------------------------
	Decode:
	['\t\x0f\x15\x08', '\x07\x0c\x0e\x05', '\x0f@\x01B']
	h 0x9 ^ 0x61 ^ 0x0 = 0x68
	l 0xf ^ 0x61 ^ 0x2 = 0x6c
	w 0x15 ^ 0x61 ^ 0x3 = 0x77
	l 0x8 ^ 0x61 ^ 0x5 = 0x6c
	e 0x7 ^ 0x62 ^ 0x0 = 0x65
	o 0xc ^ 0x62 ^ 0x1 = 0x6f
	o 0xe ^ 0x62 ^ 0x3 = 0x6f
	d 0x5 ^ 0x62 ^ 0x3 = 0x64
	l 0xf ^ 0x63 ^ 0x0 = 0x6c
	  0x40 ^ 0x63 ^ 0x3 = 0x20
	r 0x1 ^ 0x63 ^ 0x10 = 0x72
	! 0x42 ^ 0x63 ^ 0x0 = 0x21
	['hlwl', 'eood', 'l r!']
	hello world!

---

#### Finding the key

Now that we can decode, we still need to know the key.

Notice that the very first character instance in each chunk is `CHAR ^ KEY ^ 0x00`

This means that the first character instance for the length of the key is just a simple XOR with no carryover.

We can reverse the first 6 chars of the key assuming `tjctf{` as the starting.

	# 473c23192d47
	# tjctf

	>>> chr(ord('t') ^ 0x47)
	'3'
	>>> chr(ord('j') ^ 0x3c)
	'V'
	>>> chr(ord('c') ^ 0x23)
	'@'
	>>> chr(ord('t') ^ 0x19)
	'm'
	>>> chr(ord('f') ^ 0x2d)
	'K'
	>>> chr(ord('{') ^ 0x47)
	'<'

Hence, the partial key is `3V@mK<`.

---

I manually tried various key length. A key length of 8 produces a pretty legible results so I assumed the 2 missing characters.

	$ python3 solver.py 
	ciphertext length: 56
	key multiple: 7.0
	key: 3V@mK<__
	tjctf{h]ybe_Wr43ing_m\63ncRypQX0N_MY5`f_W4Snq6v_sm4R2

Now I bruteforced the last 2 chars and manually scanned through the results to find the flag most legible

	key: 3V@mK<Z6
	decode: tjctf{m4ybe_Wr1t3ing_mY_3ncRypT10N_MY5elf_W4Snt_v_sm4R7}

## Flag

	tjctf{m4ybe_Wr1t3ing_mY_3ncRypT10N_MY5elf_W4Snt_v_sm4R7}
