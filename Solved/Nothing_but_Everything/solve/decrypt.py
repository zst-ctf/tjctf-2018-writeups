#!/usr/bin/env python3
import os


def get_files():
    for (dirpath, dirnames, filenames) in os.walk("./1262404985085867488371"):
        for filename in filenames:
            path = dirpath + "/" + filename
            yield (path, filename)


def decrypt_int(decimal):
    decimal = int(decimal)
    hex_string = '{0:x}'.format(decimal)
    text = bytes.fromhex(hex_string)
    return text


def decrypt_file(path):
    with open(path) as f:
        content = f.read().strip()
    return decrypt_int(content)

if __name__ == '__main__':
    for path, filename in get_files():
        if 'HAHAHA.txt' in filename:
            continue

        filename_dec = decrypt_int(filename).decode()
        path_dec = path.replace(filename, filename_dec)
        contents_dec = decrypt_file(path)

        with open(path_dec, 'wb') as f:
            f.write(contents_dec)

        print("Decrypted:", path)
        print("Generated:", path_dec)
        print("")
