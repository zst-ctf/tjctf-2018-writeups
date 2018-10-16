# Validator
Reverse Engineering - 30 points

## Challenge 

Written by evanyeyeye

I found a [flag validation program](412108f24d79f657ca3ff30fdf436ffa73d1e14a5d9ea0de63e917b8c1dc1528_flagcheck). Do what you want with it.

## Solution

Hopper Decompiler


	int main(int arg0) {
	    ebp = (esp & 0xfffffff0) - 0x8;
	    esp = (esp & 0xfffffff0) - 0x50;
	    *(ebp + 0xffffffc4) = *(&arg0 + 0x4);
	    *(ebp + 0xfffffff4) = *0x14;
	    *(ebp + 0xffffffc8) = 0x74636a74;
	    *(ebp + 0xffffffcc) = 0x756a7b66;
	    *(ebp + 0xffffffd0) = 0x635f3735;
	    *(ebp + 0xffffffd4) = 0x5f6c6c34;
	    *(ebp + 0xffffffd8) = 0x725f336d;
	    *(ebp + 0xffffffdc) = 0x72337633;
	    *(ebp + 0xffffffe0) = 0x365f3335;
	    *(ebp + 0xffffffe4) = 0x665f6430;
	    *(ebp + 0xffffffe8) = 0x5f6d3072;
	    *(ebp + 0xffffffec) = 0x5f77306e;
	    *(ebp + 0xfffffff0) = 0x7d6e30;
	    if (arg0 == 0x2) {
	            esp = (esp - 0x10) + 0x10;
	            if (strlen(*(*(ebp + 0xffffffc4) + 0x4)) == 0x2b) {
	                    *(int8_t *)(ebp + 0xffffffdb) = 0x33;
	                    *(int8_t *)(ebp + 0xffffffde) = 0x33;
	                    *(int8_t *)(ebp + 0xffffffe0) = 0x33;
	                    *(int8_t *)(ebp + 0xffffffdc) = 0x35;
	                    *(int8_t *)(ebp + 0xffffffdd) = 0x72;
	                    *(int8_t *)(ebp + 0xffffffe1) = 0x72;
	                    *(int8_t *)(ebp + 0xffffffdf) = 0x76;
	                    esp = (esp - 0x10) + 0x10;
	                    if (strcmp(ebp + 0xffffffc8, *(*(ebp + 0xffffffc4) + 0x4)) == 0x0) {
	                            puts("Valid flag.");
	                    } else {
	                            puts("Invalid flag.");
	                    }
	            } else {
	                    puts("Invalid flag.");
	            }
	    } else {
	            printf("Usage: %s <flag>\n", **(ebp + 0xffffffc4));
	    }

	    //...
	}

Retrieve the values from the array

	>>> from pwn import *
	>>> x = [0x74636a74, 0x756a7b66, 0x635f3735, 0x5f6c6c34, 0x725f336d, 0x72337633, 0x365f3335, 0x665f6430, 0x5f6d3072, 0x5f77306e, 0x7d6e30]

	>>> ''.join(map(lambda a: p32(a), x))
	'tjctf{ju57_c4ll_m3_r3v3r53_60d_fr0m_n0w_0n}\x00'

But this is not the flag

---

There's another portion. It replaces some values in the original array.
	                    
    *(int8_t *)(ebp + 0xffffffdb) = 0x33;
    *(int8_t *)(ebp + 0xffffffde) = 0x33;
    *(int8_t *)(ebp + 0xffffffe0) = 0x33;
    *(int8_t *)(ebp + 0xffffffdc) = 0x35;
    *(int8_t *)(ebp + 0xffffffdd) = 0x72;
    *(int8_t *)(ebp + 0xffffffe1) = 0x72;
    *(int8_t *)(ebp + 0xffffffdf) = 0x76;

So since the flag starts at `0xffffffc8`, the offset/index is as follows

    [19] = 0x33; // 3
    [22] = 0x33; // 3
    [24] = 0x33; // 3
    [20] = 0x35; // 5
    [21] = 0x72; // r
    [25] = 0x72; // r
    [23] = 0x76; // v

Now get the correct flag

	>>> x = list("tjctf{ju57_c4ll_m3_r3v3r53_60d_fr0m_n0w_0n}")
	>>> x[19] = chr(0x33);
	>>> x[22] = chr(0x33);
	>>> x[24] = chr(0x33);
	>>> x[20] = chr(0x35);
	>>> x[21] = chr(0x72);
	>>> x[25] = chr(0x72);
	>>> x[23] = chr(0x76);
	>>> ''.join(x)
	'tjctf{ju57_c4ll_m3_35r3v3r_60d_fr0m_n0w_0n}'

## Flag

	tjctf{ju57_c4ll_m3_35r3v3r_60d_fr0m_n0w_0n}
