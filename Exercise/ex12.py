age = raw_input("How old are you? ")

height = raw_input("How tall are you? ")

weight = raw_input("How much do you weigh? ")

print "----------use %---------------"
print "So,you're %r old, %r tall and %r heavy." %(age,height,weight)
print "----------use .format---------------"
print "{} old, {} tall, {} heavy." .format(age,height,weight)