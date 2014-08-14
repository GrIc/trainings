# -*- coding: utf-8 -*-
print "How old are you ?",
age = int(raw_input())
print "How tall are you ?",
height = int(raw_input())
print "How much do you weight ?",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "Sum of that is %d !" % (age + height + weight)
