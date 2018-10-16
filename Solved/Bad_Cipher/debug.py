DEBUG = False

def pad_hex_pair(f):
    '''
    Returns a hex pair string of the ascii `f`.

    1<<8 is 0x100
    Hence, it makes it always 0x1?? where ?? is the ascii code
    Then cut out the first 3 chars to get ??
    '''
    return hex( (1<<8)+ord(f) )[3:]


def split_chunks(msg, key_length):
    return [msg[i::key_length] for i in range(key_length)]


def join_chunks(chunks):
    x = "".join
    return x(pad_hex_pair(f) for f in x(x(y)for y in zip(*chunks)))


def encode(msg, key):
    key_length = len(key)

    # split the chars into chunks of alternating array
    s = split_chunks(msg, key_length)
    if DEBUG: print(s)

    # for each chunk, apply xor but dependent on previous char
    for i in range(key_length):
        a = 0
        e = ""

        for c in s[i]:
            if DEBUG: print(c, f"{hex(ord(c))} ^ {hex(ord(key[i]))} ^ {hex(a>>2)} =", hex(ord(c) ^ ord(key[i]) ^ (a>>2)))
            a = ord(c) ^ ord(key[i]) ^ (a>>2)
            e += chr(a)

        s[i] = e
    if DEBUG: print(s)

    # join back chunks
    return join_chunks(s)


def decode(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext).decode()
    key_length = len(key)

    # split
    s = split_chunks(ciphertext, key_length)
    if DEBUG: print(s)

    # un-xor
    for i in range(key_length):
        a = 0
        e = ""

        for c in s[i]:
            decrypt = ord(c) ^ ord(key[i]) ^ (a>>2)
            if DEBUG: print(chr(decrypt), f"{hex(ord(c))} ^ {hex(ord(key[i]))} ^ {hex(a>>2)} =", hex(decrypt))
            
            e += chr(decrypt)
            a = ord(c)

        s[i] = e

    if DEBUG: print(s)

    # join back
    return bytes.fromhex(join_chunks(s)).decode()

if __name__ == '__main__':
    DEBUG = True
    message = "hello world!"
    key = "abc"

    print("------------------------------")
    print("Encode:")
    print(encode(message,key))

    print("------------------------------")
    print("Decode:")
    print(decode("09070f0f0c40150e01080542",key))
