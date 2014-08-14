# -*- coding: utf-8 -*-

#import argv
from sys import argv

#get script name and first arg
script, filename = argv

#create a file, instiate with filename path
txt = open(filename)

#say the user the file was found
print "Here's your file: %r" % filename
#print on the console the content of the file
#print txt.read()
for l in txt.readlines():
        print l,

#print "Type the filename again:"
##retrieve another file path
#file_again = raw_input("> ")
#
##store the new file in txt_again, print its content
#txt_again = open(file_again)
#print txt_again.read()
txt.close()
