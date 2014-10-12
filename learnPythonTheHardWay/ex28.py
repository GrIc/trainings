# -*- coding: utf-8 -*-
print (True and False)
print "False"

print (False and True)
print "False"

print (1 == 1 and 2 == 1)
print "False"

print ("test" == "test")
print "True"

print (1 == 1 or 2 != 1)
print "True"

print (True and 1 == 1)
print "True"

print (False and 0 != 0)
print "False"

print (True or 1 == 1)
print "True"

print ("test" == "testing")
print "False"

print ("test" == 1)
print "False"

print (not(True and False))
print "True"

print (not (1 == 1 and 0 != 1))
print "False"

print (not (10 == 1 or 1000 == 1000))
print "False"

print (not(1 != 10 or 3 == 4))
print "False"

print (not("testing" == "testing" and "Zed" == "Cool Guy"))
print "True"

print (1 == 1 and (not ("testing" == 1 or 1 == 0)))
print "True"

print ("Chunky" == "bacon" and (not(3 == 4 or 3 == 3)))
print "False"

print (3 == 3 and (not("testing" == "testing" or "Python" == "fun")))
print "False"
