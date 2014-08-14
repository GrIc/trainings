# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r adds single quotes to the output if it is a string -> raw data, NEVER use in prod
print "I said: %r." % x
#%s does not add the single quotes -> need to add it explicitly
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side !"

print w + e