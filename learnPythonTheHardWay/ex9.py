# -*- coding: utf-8 -*-
#Here's some new strange stuff

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months
#the following does not traduce '\n' as a line break
print "Here are the months: %r" % months
#the following does
print "Here are the months: %s" % months

print """
There's something going on here.
with the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""