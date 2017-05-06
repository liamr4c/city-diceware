#!/usr/bin/env python3
import csv

# wat
import sys
csv.field_size_limit(sys.maxsize)

with open('cities1000.txt') as f:
    r = csv.reader(f, delimiter="\t")
    with open('cities.txt', 'w') as nf:
        for row in r:
            # [1] is "name of geographical point (utf8) varchar(200)"
            # [2] is that BUT IN ASCII.
            # Because we want to be able to type these on a normal keyboard, we
            # will use [2]
            nf.write(row[2])
            nf.write("\n")

