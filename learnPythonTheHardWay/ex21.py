# -*- coding: utf-8 -*-
def add(a, b):
    print "ADDIND %d + %d" % (a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with functions"

age = add(30, 5)
height = subtract(180, 7)
weight = multiply(31, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %s, IQ: %d" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand ?"
