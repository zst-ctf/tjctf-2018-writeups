# Online Banking
Binary Exploitation - 90 points

## Challenge 

Written by nthistle

Try out our new online banking service!

nc problem1.tjctf.org 8005

[Binary](b227d63762bf31ccd91aba57d50ab405d5dbe252a43b39acc9d86b6e2fdf74e3_problem) 

[Source](c78eed9e241b2e36eacd5f86a715cbde06ee4c51c66603734dea7fc2e9c32669_problem.c)

## Solution

Exploit is here. `fgets()` uses the wrong array size.

	int verify_pin(char* pin) {
	    char pin_check[PIN_SIZE+1];
	    printf("Please verify your PIN first:\nPIN: ");
	    fgets(pin_check, NAME_SIZE+1, stdin);
	    for(int i = 0; i < 4; i ++) {
	        if(pin[i] != pin_check[i])
	            return 0;
	    }
	    return 1;
	}

We can override the return address and return to libc system()



	# gdb ./problem 
	
	(gdb) b main    
	Breakpoint 1 at 0x4007df

	(gdb) r
	Starting program: /FILES/problem 

	Breakpoint 1, 0x00000000004007df in main ()
	(gdb) p system
	$1 = {int (const char *)} 0x7ffff7e4e5d0 <__libc_system>

	(gdb) p verify_pin
	$2 = {<text variable, no debug info>} 0x400767 <verify_pin>

	(gdb) p printf    
	$3 = {int (const char *, ...)} 0x7ffff7e61ed0 <__printf>


https://stackoverflow.com/questions/7772847/return-to-libc-exploit-where-to-provide-arguments-for-system-call

https://security.stackexchange.com/questions/121922/return-to-libc-cant-get-the-system-function-address

https://www.exploit-db.com/docs/english/28553-linux-classic-return-to-libc-&-return-to-libc-chaining-tutorial.pdf


## Flag

	??