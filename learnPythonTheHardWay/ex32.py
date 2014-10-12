# -*- coding: utf-8 -*-
the_count = [ 1, 2, 3, 4, 5 ]
fruits = [ 'apples', 'oranges', 'pears', 'apricots' ]
change = [ 1, 'pennies', 2, 'dimes', 3, 'quarters' ]

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d." % number

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r." % i

# we can also build lists, first start with an empty one
elements = []

# then populate
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

# now, display what we got
for i in elements:
    print "Element contains: %d" % i
