#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(n):
    """ returns the sequence of n fibonacci numbers
    """
    firstfib = 1
    secondfib = 1
    temp = 0
    seq = ""
    for i in range (n+1):
        seq += (firstfib + " ")
        temp = secondfib + firstfib
        firstfib = secondfib
        secondfib = temp
    return seq
    
