#!/usr/bin/env python

# This reducer takes input from heatMapper.py in the form of four numbers per
# line as the coordinates for a found word on a front page of The Times.
# These are loaded into an array which is the single output of this reducer.
# A third program called heatPlot.py takes the output and produces the plot.

from operator import itemgetter
import sys

import numpy as np
#frontPage = np.zeros((7000,4850))
frontPage = np.zeros((1000,1000))
#frontPage.dtype
frontPage = frontPage.astype('uint32')
#frontPage.dtype
print(frontPage)

# input comes from STDIN
# for line in sys.stdin:

# Need to use a regular file for testing
with open("sampleMapperOutput.txt", "r") as f:
    for line in f:
        line = line.strip('\n')

        try:
            posList = str(line).split(',')
            #print(posList)
            posList = [int(item) for item in posList]
            #print(pos,posList)
            frontPage[posList[1]:posList[3],posList[0]:posList[2]] += 1
        except:
            continue

"""
import numpy as np
a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
a.tofile('foo.csv',sep=',',format='%10.5f')
"""
print frontPage
#with open("sampleReducerOutput.csv","w") as f:
    #frontPage.tofile(f,sep=',')
    #np.savetxt(f,frontPage,fmt='%10000u',delimiter=",")
    #np.savetxt(f,frontPage,delimiter=",")


"""
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_word == word:
            current_count += count
        else:
            if current_word:
                # write result to STDOUT
                print '%s\t%s' % (current_word, current_count)
            current_count = count
            current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
"""
