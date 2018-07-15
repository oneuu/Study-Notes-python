formatter = "{} {} {} {}"
formatter1 = "%r %r %r %r"


print formatter .format(1,2,3,4)
print formatter .format("one","two","three","four")
print formatter .format(True,False,True,False)
print formatter .format(formatter,formatter,formatter,formatter)
print formatter .format(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So i said goodnight.")
print "\n"
print "\n"
print formatter1 %(1,2,3,4)
print formatter1 %("one","two","three","four")
print formatter1 %(True,False,True,False)
print formatter1 %(formatter,formatter,formatter,formatter)
print formatter1 %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So i said goodnight.")
