#!/usr/bin/env python3
import secrets
import argparse

parser = argparse.ArgumentParser(description='Generate a diceware-like password from `cities.txt`')
parser.add_argument('--words', '-n', type=int, nargs='?', 
        dest='NUMWORDS', default=5, help='Number of words')
parser.add_argument('--delimiter', '-d', type=str, nargs='?', 
        dest='DELIMITER', default="-", help='Delimiter')
parser.add_argument('--lower', '-l', action="store_true",
        dest='LOWER', default=False, help='Lowercase the output')

args = parser.parse_args()

words=[]

with open('cities.txt') as f:
    words+=f.read().splitlines()

for i in range(0, args.NUMWORDS):
    word=secrets.choice(words)
    if args.LOWER:
        word=word.lower()
    print(word, end='')
    if i+1!=args.NUMWORDS:
        print(args.DELIMITER, end='')

print("")# Newline
