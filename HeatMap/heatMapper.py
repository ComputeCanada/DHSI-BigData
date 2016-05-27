#!/usr/bin/env python

# This mapper reads OCR scans from The Times, finds a given word, and
# outputs the page coordinates for each find on a single line.
# The output is to be picked up by heatReducer.py

import sys
import re

searchTerm = "war"
searchTerm = searchTerm.lower()
regEx = re.compile(r"<wd pos=\"(\d+,\d+,\d+,\d+)\">([\w\'\",\[\]\{\}\(\)\.]+)</wd>")

# will need RegEx since using STDIN and not lxml so won't have access to tree
# General process:
# 1. match line to <wd pos="(\d+,\d+,\d+,\d+)">([\w'",\[\]\(\)\{\}\.])+</wd>
# 2. extract word group.
# 3. convert word group to lowercase.
# 4. if word group matches searchTerm then output the coordinates
# 5. next line

# input comes from STDIN (standard input)
#for line in sys.stdin:

# read from regular file for testing

with open("SmallTestDataSet.xml", "r") as f:
    for line in f:
        try:
            # remove leading and trailing whitespace
            line = line.strip()
            m = re.search(regEx, line)
            if m != None:
                #print(m.group(0),m.group(1),m.group(2))
                if m.group(2).lower() == searchTerm:
                    print m.group(1)
            """
            # increase counters
            for word in words:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                print '%s\t%s' % (word, 1)
            """
        except:
            continue
