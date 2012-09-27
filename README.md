file-checksum-checker
=====================

Finds files and checks their checksum against a list provided as input.

Right now, all it does is:
  * Read the file given as argument, which should consist of a list of checksums followed by the filename
  * Searches the current directory recursively (using python's os.path.walk) for the file
  * If the file is found, calculates the file MD5 and compares with the one in the list

Usage:
    ./file-checksum-checker checksumlist.txt

Checksum file list example:
f768cb5cd8277268c91a806770617d3c README.md
dbcfddfc48b137ad5e9ae165c88bbbc9 file-checksum-checker.py

