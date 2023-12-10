Advent of Code 2023
===================

The program must be run as a module:

    python -m aoc2023 -d DAY -p PART [-z] [-v] [-h]

By default, the program will use the file _puzzle\<DAY\>\_part\<PART\>.txt_ as input. You can override it using the option _-z_ :

    python -m aoc2023 -d 3 -p 1 -z aoc2023/day3/example.txt

Logger level
------------

* -v : error
* -vv : warning
* -vvv : info
* -vvvv : debug
* -vvvvv : spam