from sys import argv

script,user_name = argv
prompt = '>>> '

print "Hi, %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
comp = raw_input(prompt)

print """
Alright so you said {} about liking me.
you live in {}.I'm not sure where that is.
And you have a {} computer.Nice bro.
""" .format(likes,lives,comp)
