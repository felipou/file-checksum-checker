#!/usr/bin/python

from os.path import walk, join
import sys
import hashlib

lines = open( sys.argv[1] ).readlines()

checksums = {}
for l in lines:
    (c, n) = l.split(" ")
    checksums[ n[:len(n)-1] ] = c

def file_md5(f, block_size=2**20):
    md5 = hashlib.md5()
    data = f.read(block_size)
    while data:
        md5.update(data)
        data = f.read(block_size)
    return md5.digest()

filesfound = []
def visit(arg, dirname, names):
    for x in [x for x in names if x in checksums.keys()]:
        filepath = join(dirname, x)
        checksum = checksums[x]
        checksum_calc = file_md5(open(filepath)).encode("hex")
        filesfound.append(x)
        
        if checksum == checksum_calc:
            print "File checksum correct:", x
        else:
            print "!!!! File checksum INCORRECT:", x

walk(".", visit, None)

for f in checksums.keys():
    if f not in filesfound:
        print "File not found:", f

