#!/usr/bin/env python3
import numpy as np

max_length = 200
# Get random number array
np.random.seed(12345)
other = [x for x in np.random.randint(1,5,(max_length))]

# Convert bin text to hex text
cipher_hex = hex(0b1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101)
cipher_hex = hex(0b10011000010111101101000011000010100000111)
cipher_hex = cipher_hex[2:]  # remove prepended 0x


def decrypt_char(val, index):
    # XOR cipher
    lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
    ch = (val ^ lmao[index])

    # un-multiply
    ch /= other[index]

    print(ch)

    if ch.is_integer():
        return chr(int(ch))
    else:
        return None


flag = ''
for index in range(max_length):
    multiplied = other[index]

    if False and multiplied <= 2:
        # within 8-bits
        ch = int(cipher_hex[:2], 16)  # get 2 char for myself
        cipher_hex = cipher_hex[2:]  # then remove from pending array
        result = decrypt_char(ch, index)
        
        assert result is not None, f"{hex(ch)} / {multiplied}"
        flag += result
    
    else:  # 12-bits or 8-bits
        # try 8-bits first
        hex_str = cipher_hex[:2]
        cipher_hex = cipher_hex[2:]
        ch = int(hex_str, 16)
        result = decrypt_char(ch, index)

        # else take one more char for 12-bits
        if result is None:            
            hex_str += cipher_hex[:1]
            cipher_hex = cipher_hex[2:]
            ch = int(hex_str, 16)
            result = decrypt_char(ch, index)

        assert result is not None
        flag += result

    print(flag)

    if len(cipher_hex) == 0:
        print(flag)
        quit()
