#!/usr/bin/python3

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Фильтрация строк в файле по правилу')
parser.add_argument('-f', help='файл для чтения', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('rule', choices=['contains', 'startswith', 'endswith'], help='Правило для фильтрации')
parser.add_argument('tokens', nargs='+', help='Правило для фильтрации')
args = parser.parse_args()

for line in args.f:
    for token in args.tokens:
        if args.rule == 'contains' and re.search(token, line):
            print(line)
            break
        elif args.rule == 'startswith' and re.search(token, line):
            print(line)
            break
        elif args.rule == 'endswith' and re.search(token, line):
            print(line)
            break
