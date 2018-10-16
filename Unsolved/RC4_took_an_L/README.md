# RC4 took an L
Cryptography - 40 points

## Challenge 

Written by evanyeyeye

Alphabet: `#_23456789abcdefghijklmnopqrstuvwxyz`

Key: `pq_xc589r3nb#mgjtkh7w2dlfvy4eaoi6uzs`

Ciphertext: `wpwt#5ng4_qbitp#8mq59r_g866c4t59c6vy6tisj4af6bprfnbd_wrq2wjmr4ld_s26a7i#biiyqjolq8lus_wfusfkj8xv2qrrv3etab_marovc#uuoueyl`

## Solution

https://gist.github.com/cosu/4017169


Python 3.6.3 (default, Oct  4 2017, 06:09:38) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Cipher import ARC4
>>> decr = ARC4.new(key).decrypt(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'key' is not defined
>>> 
>>> key = key = 'pq_xc589r3nb#mgjtkh7w2dlfvy4eaoi6uzs'
>>> data = 'wpwt#5ng4_qbitp#8mq59r_g866c4t59c6vy6tisj4af6bprfnbd_wrq2wjmr4ld_s26a7i#biiyqjolq8lus_wfusfkj8xv2qrrv3etab_marovc#uuoueyl'
>>> key
'pq_xc589r3nb#mgjtkh7w2dlfvy4eaoi6uzs'
>>> data
'wpwt#5ng4_qbitp#8mq59r_g866c4t59c6vy6tisj4af6bprfnbd_wrq2wjmr4ld_s26a7i#biiyqjolq8lus_wfusfkj8xv2qrrv3etab_marovc#uuoueyl'
>>> 
>>> decr = ARC4.new(key).decrypt(data)
>>> decr
b"\xcf\x7ff\x9f\x1d\x8a\xe1Z\xa9\xde\xd0E\xef5\xe3\x19\xa7\\\xe9*\x04\xc3K\x19j1\x99\r~\xc3\x05\x12\xad\xf4lno:`\xf6,\x0f\xb7\xa4\xc7\x15|_\xf0\xd7'\x80\xb0\x16\x139J3\xf2g\x93v\xc8\x16a\x8a\xe2{\x00\xb4-\xa6-\x85\x81\xfb\xafm\xcf\xbe\x8f\x129%r.5`\xc7z\x98C\xdb\x13\xbc\xc7\xb26nZ\xa1`\x1f\xd6b@L\x89\xef\xc9\xc4\x11\x94\x14t\x81\x91\xe1\xd5Eq"

## Flag

	??