# Exercises for chapter 3:

# Name:Steve Blank

#3.1 
#def print_lyrics():								original
#	print "I'm a lumberjack, and I'm okay."			original
#	print "I sleep all night and I work all day"	original
#
#def repeat_lyrics():								original
#	print_lyrics()									original
#	print_lyrics()									original
#
#repeat_lyrics()									original

#repeat_lyrics()									new

#def print_lyrics():								new
#	print "I'm a lumberjack, and I'm okay."			new
#	print "I sleep all night and I work all day"	new

#def repeat_lyrics():								new
#	print_lyrics()									new
#	print_lyrics()									new
	
#This is the error received when running:			answer
#NameError: name 'repeat_lyrics' is not defined		answer

#3.2
def repeat_lyrics():
	print_lyrics()
	print_lyrics()	

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day"

repeat_lyrics()

#The program still seems to run okay when I switch the location of both definitions.
#I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day
#I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day
#[Finished in 0.1s]


#3.3
#print len('allen')

def right_justify(s, location):
	print (' '*(location-len(s))+s)
location = 70	
right_justify('allen', location)

#3.4.1

def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

#3.4.2

def do_four(f):
	do_twice(f)
	do_twice(f)

do_four(print_spam)

#3.4.3
def print_twice(n):
	print n
	print n
n="a string as a parameter printed twice"
print_twice(n)

#3.4.4
do_twice(print_spam)