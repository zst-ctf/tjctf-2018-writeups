# Future Canary Lab
Binary Exploitation - 80 points

## Challenge 

Written by evanyeyeye

The world renowned Future Canary Lab is looking for a new lab member. Good luck with your [interview](c962e5ec36fc4161a93c042e1837cf0fe0a35a92469f37181f827d9ee8a54cca_interview) ([source](2e1b38dc00bfb021e2deb45219f4c44b371dc1ae98b0fb2ee2d9905032e310a3_interview.c))!

`nc problem1.tjctf.org 8000`

## Solution

***I have written the solution comments in `solve.c`***

test.c and test2.c are programs for debugging values.

Test using 

	gcc test.c -o test; gcc solve.c -o solve; ./solve | ./test
	gcc test2.c -o test2; gcc solve.c -o solve; ./solve | ./test2
	gcc solve.c -o solve; ./solve | ./interview

Payload works locally

	Welcome to the Future Canary Lab!
	What is your name?
	You are the one. This must be the choice of Stacks Gate!
	Here is your flag: -----REDACTED-----


But not on the server...

---

I asked the challenge creator and the server is using libc v2.27

I tried to install it but it did not make a difference...

(Reference: https://wiki.mikejung.biz/How_to_install_Glibc-2.15_on_CentOS6)

	mkdir ~/glibc_install; cd ~/glibc_install 
	wget https://ftp.gnu.org/gnu/glibc/glibc-2.27.tar.gz
	tar zxvf glibc-2.27.tar.gz
	cd glibc-2.27
	mkdir build
	cd build
	../configure --prefix=/opt/glibc-2.27
	make -j4
	sudo make install

	export LD_LIBRARY_PATH=/opt/glibc-2.27/lib


## Flag

	??