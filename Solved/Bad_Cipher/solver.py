from debug import *
import string

ciphertext = '473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554'
key = '3V@mK<__'

# check calculations
print("ciphertext length:", len(ciphertext) // 2)
print("key multiple:", (len(ciphertext) // 2) / len(key))
print("key:", key)
print(decode(ciphertext, key))


print(">> Bruteforcing...")
for a in string.printable:
    for b in string.printable:
        key = '3V@mK<' + a + b
        dec = decode(ciphertext, key)

        # reject if not complete flag
        if not dec.endswith("}"):
            continue
        # reject if non-printable
        if not all(c in string.printable for c in dec):
            continue
        # reject if multi-lined
        if '\n' in dec or '\r' in dec:
            continue

        # else, print the possibility
        print("key:", key)
        print("decode:", dec)
