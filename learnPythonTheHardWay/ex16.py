# -*- coding: utf-8 -*-
from sys import argv

script_name, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye !"
#The truncate is unecessary because we open the file in 'write' mode
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these lines to the file."
file_content = "%s\n%s\n%s\n" % (line1, line2, line2)
target.write(file_content)

print "And finally, close the file."
target.close()

