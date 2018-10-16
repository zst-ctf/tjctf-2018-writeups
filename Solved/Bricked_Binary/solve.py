#!/usr/bin/env python3
import re


def extract_hopper_values(filename):
    with open(filename) as f:
        textfile = f.read()

    hex_str_array = re.findall(r'0x(..)', textfile)
    int_array = list(map(lambda s: int(s, 16), hex_str_array))
    return int_array


lookup_table = extract_hopper_values("0804a040.txt")
key = extract_hopper_values("0804a440.txt")

output_hash = bytes.fromhex('22c15d5f23238a8fff8d299f8e5a1c62')
length = len(output_hash)

assert length == 16

original = [''] * 16
i = 0
while i < length:
    # Reverse of: text[length - 1 - i] = lookup_table[((text[length - 1 - i] & 0xff) * 4] ^ key[i * 4];
    lookup_value = output_hash[length - 1 - i] ^ key[i * 4]
    lookup_index = lookup_table.index(lookup_value)

    # Reverse of: lookup_index = text[length - 1 - i] & 0xff) * 4
    ch = lookup_index // 4
    original[length - 1 - i] = ch
    i += 1

# convert int to chr
original = list(map(lambda numb: chr(numb), original))
print(''.join(original))
