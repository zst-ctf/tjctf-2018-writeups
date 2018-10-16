#!/bin/bash

FILE="password-list.txt"

a=($(wc "$FILE"))
lines=${a[0]}
words=${a[1]}
chars=${a[2]}

while read password; do
    unzip -P $password foremost.zip >/dev/null 2>/dev/null
    if [ -e flag.txt ]; then
        if grep -q "tjctf{" flag.txt; then
            echo " "
            echo "Password is: $password"
            cat flag.txt
            exit
        else
            rm flag.txt
        fi
    fi
    printf "\rDoing $lines"
    lines=$((lines-1))
done < "$FILE"