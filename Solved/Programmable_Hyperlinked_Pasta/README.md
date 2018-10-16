# Programmable Hyperlinked Pasta
Web - 60 points

## Challenge 

Written by nthistle

Check out my new site! PHP is so cool!

`programmable_hyperlinked_pasta.tjctf.org`

## Solution

#### Simple path traversal

We have an english site, and there's a link to a spanish site at the bottom left.

https://programmable_hyperlinked_pasta.tjctf.org/?lang=es.php

In addition, we see there's a flag.txt in the source code.

	<!-- <a href="flag.txt">Here's a flag!</a> -->

But the link to the flag is 403 Forbidden 

https://programmable_hyperlinked_pasta.tjctf.org/flag.txt

---

Try traversing up a directory using the `lang` param and we see the flag

https://programmable_hyperlinked_pasta.tjctf.org/?lang=../flag.txt


## Flag

	tjctf{l0c4l_f1l3_wh4t?}
