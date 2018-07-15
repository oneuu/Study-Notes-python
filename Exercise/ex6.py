x = "there are {} type of people." .format(10)

binary = "binary"
do_not = "don't"

y = "those who know {} and those who {}" .format(binary,do_not)

print x
print y
print '---------------'

print "I said: {}".format(x)
print "I also said: {:s}".format(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print joke_evaluation .format(hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print w+e
