#!/bin/bash

for i in $(seq 10000); do
    ./fib.py ${i} >> fibs.csv
done
