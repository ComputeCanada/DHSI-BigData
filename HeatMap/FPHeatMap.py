# This script reads through the OCR output of the London Times Digital Archive
# by Gale Cengage Learning and returns a heat map showing the relative
# frequency with which a give word appears on the front page.
# Originally produced to be used with a Big Data Analysis course at the
# Digital Humanities Summer Institute in 2016.
# Orignial idea by Pawel Pomorski.  Initial coding by John Simpson.

# CODE OVERVIEW: The program use a rectangular numpy array to represent the
# front page of a newspaper.  When given an word to search for the program
# searches through the page scans, finding each word and the area on the page
# on which the word was found.  All cells within the front page array that
# overlap with that location are incremented.  When all instances have been
# found and the all increments made the array is then passed to matplotlib to
# generate a simple heatmap.

import numpy
