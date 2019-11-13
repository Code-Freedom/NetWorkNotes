import sys
import os

fname = input("please inpute filename:")
while fname != 'end':
    print(fname)
    fname = input("please inpute filename:")
    open(fname, 'w')
