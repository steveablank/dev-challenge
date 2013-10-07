# Exercises for chapter 2:

# Name:Steve Blank

# Exercise 2.1
zipcode = 02132
print zipcode
zipcode2 = '02132'
print zipcode2
zipcode3 = 01
print zipcode3
zipcode4 = 010
print zipcode4
zipcode5 = 0100
print zipcode5
zipcode6 = 01000
print zipcode6

#Leading zero causes number to be octal.  


# Exercise 2.2

#>>> 5
#5
#>>> x=5
#>>> x + 1
#6
#>>> 

5
x = 5
x + 1

print 5
print 'x = 5'
print x
print x + 1
print (x + 1)
print ('x + 1')


# Exercise 2.3
# Assignment Statements
width=17
height=12.0
delimiter='.'

# Print Statements
print width/2			#8
print type((width/2))	#<type 'int'>
print width/2.0  		#8.5
print type(width/2.0)	#<type 'float'>
print height/3			#4.0
print type(height/3)	#<type 'float'>
print 1+2*5				#11	
print type(1+2*5)		#<type 'int'>
print delimiter*5		#'.....'
print type(delimiter*5)	#<type 'str'>


# Exercise 2.4
#1) Volume (r) = 4/3 pi r^3

pi = 3.141592653589793
r = 5.0
x = (4.0/3.0)
#= (x)*pi*r^3  PEMDAS

print x * pi * (r**3)	#523.598775598

#2) 
book = 24.95
discount = .40 * book
dbook = book - discount
ship1st = 3.0
shipall = 0.75
n = 60
totalcost = ship1st + ((n-1)*shipall) + (n*dbook)
print totalcost			#945.45

#3)
leavehour = 6
leavemin = 52
leavesec = 0

easymin = 8
easysec = 15
tempomin = 7
temposec = 12
easymiles = 2
tempomiles = 3

tempominutes = tempomiles * tempomin
temposeconds = tempomiles * temposec
easyminutes = easymiles * easymin
easyseconds = easymiles * easysec

totalminutes = tempominutes + easyminutes	#37
totalseconds = temposeconds + easyseconds	#66
extramin = (totalminutes/60)				#0
extrasec = (totalseconds/60)				#1
adjminutes = totalminutes + extrasec		#38
adjseconds = totalseconds 					#66
arrivesec = adjseconds - 60
print arrivesec
arrivemin = 120-(leavemin + adjminutes)
print arrivemin
arrivehour = leavehour + 1
print arrivehour
print "You arrive home at %s:%s:" % (arrivehour, arrivemin) +"0"+"%s AM" %(arrivesec)
