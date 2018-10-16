# Bricked Binary
Reverse Engineering - 80 points

## Challenge 

Written by evanyeyeye

Earlier, I input my flag to this [image](674de237660f29c75cd031ea48700c170743e3a924d2fb3d4d4a981102e80c43_hashgen) and received 22c15d5f23238a8fff8d299f8e5a1c62 as the output. Unfortunately, later on I broke the program and also managed to lose my flag. Can you find it for me?

*The flag is not in standard flag format.*

## Solution

Hopper Decompiler

    int main(int arg0) {
        ebp = (esp & 0xfffffff0) - 0x8;
        esp = (esp & 0xfffffff0) - 0x20;
        ebx = &arg0;
        if (*ebx <= 0x1) {
                printf("Usage: %s <secret>\n", **(ebx + 0x4));
                eax = 0x1;
        } else {
                *(ebp + 0xfffffff4) = 0x8048684;
                strcpy(*(*(ebx + 0x4) + 0x4), *(ebp + 0xfffffff4));
                hash(*(*(ebx + 0x4) + 0x4));
                esp = ((esp - 0x10) + 0x10 - 0x10) + 0x10;
                *(ebp + 0xfffffff0) = 0x0;
                do {
                        esp = (esp - 0x10) + 0x10;
                        if (strlen(*(*(ebx + 0x4) + 0x4)) <= *(ebp + 0xfffffff0)) {
                            break;
                        }
                        printf("%02hhx", sign_extend_32(*(int8_t *)(*(ebp + 0xfffffff0) + *(*(ebx + 0x4) + 0x4)) & 0xff));
                        esp = (esp - 0x10) + 0x10;
                        *(ebp + 0xfffffff0) = *(ebp + 0xfffffff0) + 0x1;
                } while (true);
                putchar(0xa);
                eax = 0x0;
        }
        return eax;
    }

    int hash(int arg0) {
        stack[2048] = arg0;
        esp = (esp - 0x10) + 0x10;
        var_10 = strlen(arg0);
        var_14 = 0x0;
        do {
                eax = var_14;
                if (eax >= var_10) {
                    break;
                }
                *(int8_t *)((var_10 - 0x1 - var_14) + arg0) = *(sign_extend_32(*(int8_t *)(arg0 + (var_10 - 0x1 - var_14)) & 0xff) * 0x4 + 0x804a040) ^ *(var_14 * 0x4 + 0x804a440);
                var_14 = var_14 + 0x1;
        } while (true);
        ebx = var_4;
        return eax;
    }


Simplify and refactor

    void main(int argc, char * argv[]) {
        if (argc <= 1) {
            printf("Usage: %s <secret>\n", argv[0]);
            return 1;
        }

        // Empty the buffer
        *(ebp + 0xfffffff4) = 0x8048684; // 0x00 ; '.' 
        strcpy(buffer, *(ebp + 0xfffffff4)); // buffer = argv[4]

        // put hash into buffer
        hash(buffer);
        
        iter = 0; // *(ebp + 0xfffffff0) = 0x0;

        // Print hex-pair for each byte of string
        // ie. Print hex-encoded of the string in buffer
        do {
            if (strlen(buffer) <= iter) {
                break;
            }
            printf("%02hhx", buffer[iter] & 0xff);
            iter++;
        } while (true);

        putchar(0xa);

        return 0;
    }

    void hash(char * text) {
        length = strlen(text);
        i = 0x0;
        do {
            if (i >= length) {
                break;
            }

            *(int8_t *)((length - 0x1 - i) + text) = 
            *(sign_extend_32(*(int8_t *)(text + (length - 0x1 - i)) & 0xff) * 0x4 + 0x804a040) ^ *(i * 0x4 + 0x804a440);
            
            // text[length - 1 - i] = 
            // 0x804a040[((text[length - 1 - i] & 0xff) * 4] ^ 0x804a440[i * 4];
            
            i++;
        } while (true);
    }

---

#### Analysis of code

These are what I know:

- In `main()`: the program is "broken" because buffer is **emptied** before hashing.
- In `hash()`: hash is an XOR of a key at `0x804a440` and a lookup_table at `0x804a040` (lookup the char from the input)
- Array of key and lookup_table are 32-bits (4 bytes) wide.
- Length of hash = length of input 

*With hash output of `22c15d5f23238a8fff8d299f8e5a1c62`, we know the input length is 16 bytes*

#### Reversing the hash algorithm

So now I extracted out the byte table from Hopper. I will use it in my script to retrieve the values accordingly.

- `0804a040.txt` for lookup_table
- `0804a440.txt` for key

And since we know the output, we can xor the `output` with the `lookup_table` and then check the lookup table for the ascii value.

    // hash algorithm
    text[length - 1 - i] = 0x804a040[((text[length - 1 - i] & 0xff) * 4] ^ 0x804a440[i * 4];
    OR
    output_char = lookup[input_char * 4] ^ key[i*4]

    // reverse hash
    output_char ^ key[i*4] = lookup_value
    THEN search for `index` of `lookup_value` in `lookup_table`
    FINALLY input_char = index / 4 

#### Solver

Putting all into a script, it is finally solved

    $ python3 solve.py 
    yummy_h45h_br0wn

## Flag

    yummy_h45h_br0wn
