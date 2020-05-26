#!/usr/bin/env python

'''
newpost.py
Copyright 2020 Byron Wong
Contact: 90ksoon@gmail.com
This script takes in the argument as title and generates a post template.
No plugins required.
'''

import os
import sys
import re
from datetime import date

post_dir = '_posts/'

today = date.today()

if len(sys.argv) == 0:
    print("argument not passed. Pass in post name as first argument")
    exit

argument = sys.argv[1]

postslug = argument.lower().replace(' ', '-')

re.sub('[\'!@#$]', '', postslug)

filename = today.strftime('%Y-%m-%d') + '-' + postslug + '.md'

f = open(post_dir + filename, "w")

header = '---\nlayout: post\ntitle: \"' + argument + '\"\ntags: \ndate: ' + today.strftime('%Y-%m-%d %H:%M:%S %Z') + '\n---\n'

f.write(header)

f.close()

print("Post template generated")