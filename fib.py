#!/usr/bin/env python3

import sequences as sq

def main(argv):
    try:
        fib_seq = sq.fibonacci(int(sys.argv[1]))
        print(fib_seq[-1])
    except Exception as e:
        print (e)
    
if __name__ == "__main__":
    import sys
    main(sys.argv)
