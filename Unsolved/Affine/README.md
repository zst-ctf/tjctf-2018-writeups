# Affine
Cryptography - 90 points

## Challenge 

Written by etherlyt

Bob really needs to send a secret message to his friends, but Alice warned him that textbook RSA is dangerous! A very concerned Bob remembered that hashing always makes everything more secure so he added the SHA1 of the modulus to his message before encryption. Now with hashing, it must be impossible to decrypt! [cipher.txt](5e2d0035e3f245dddbd500b9846505e9c4c27bcfe11f78e8c7b62934e4b4bdf5_cipher.txt)


Clarification: The modulus is hashed as a string 

Clarification: "added" means addition not concatenation

## Solution


	Encrypt: (n, e)
	 
	c = m^e mod n

	e = 7
	c = (m+sha1(n))^7 mod n


## Flag

	??