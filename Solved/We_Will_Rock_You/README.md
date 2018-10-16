# We Will Rock You
Forensics - 75 points

## Challenge 

Written by Alaska47

Help! I lost the password to my [Dogecoin wallet](9d7e6203fb6e2c14646c63bea94e48001b9317c86bec229c3e063904a168dfad_wallet.dat). I had like 10 Dogecoin in there. If you get the password, you'll get the flag! Flag format: `tjctf{password}`

## Solution

Title implies that we need the rockyou password list. We also need a package to bruteforce the wallet.

I found a nice Git repo for it here!

	$ git clone https://github.com/glv2/bruteforce-wallet

	## Brew dependencies (Mac)
	$ brew install openssl
	$ cd /usr/local/include
	$ ln -s ../opt/openssl/include/openssl .

	$ brew install berkeley-db

	## Compile
	$ ./autogen.sh
	$ ./configure
	$ make

	## Download dictionary list
	$ wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
	$ bunzip2 rockyou.txt.bz2 

	## Bruteforce it!
	$ ./bruteforce-wallet -t 6 -f rockyou.txt -v 30 ../*_wallet.dat
	Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.

	Tried passwords: 63
	Tried passwords per second: 7.875000
	Last tried password: teamo

	Password found: tinkerbell

## Flag

	tjctf{tinkerbell}
