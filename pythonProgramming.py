########---------3.Text Processing and Files  -------------############
@@1: entire file
f = open('a.csv', 'r') # get a file object
data = f.read() # entire file all at once, in a text string
# print result more like the orginal file
f.close()

@@2: line by line
f = open('a.csv', r)
for line in f: # read line by line
    print(line)
f.close()

@@3. with
with open('a.csv') as f:
    data = f.read()
#Will automatically close the file when done

clean up lines:
line = "IBM","200-4-4", 23.34\n'
newLine = line.strip()# get rid of white space, does NOT change line, MUST SAVE INTO A VARIABLE
 ALL OPERATIONS ON STRINGS NEVER MODIFY THE ORIGINAL STRING!  MUST SAVE CHANGE

line.replace('"', '-')

line.split(',') # get a list of parts


## Reading a file and performing a calculation
total = 0.0
with open('a.csv', r) as f:
    headers = next(f)  # skip the header row
    for line in f:
        line = line.strip() # strip whitespace
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[2] = int(parts[2])
        #print(parts)
        total += parts[2]*parts[3]
print('Total Cost', total)


## Using the CSV module to read data

USE
STANDARD LIBRARIES
import csv # read comma seperated value files

f = open('a.csv', 'r')
rows = csv.reader(f) # will take care of splitting the rows up, do clean up steps
for row in rows:
    print(row)
# ['AA', '2003-4-3-', '234']

total = 0.0
with open('a.csv', r) as f:
    rows = csv.reader(f)
    headers = next(rows)  # skip the header row
    for line in f:
        rows[0] = parts[0].strip('"')
        rows[2] = int(parts[2])
        #print(parts)
        total += rows[2]*rows[3]
print('Total Cost', total)



########---------4.Functions and Error Handling  -------------############

## Define and use simple functions

def greeting(name):
    print('name', name)

NOTES:
everything inside the functions stay in the function, not accessible from outside

ways to call functions:

1. greeting('liu')
2. greeting(name='liu') #keyword argument passing

@Documentation String
# the doc string feeds python's help command
def greeting(name):
    """
    Issues a greeting
    """
    print(name)

help(greeting) # doc string will show up in help


## Move a script into a function

def porfoli_cost(filename):
    """
    total share of prices of a file
    """
    total = 0.0
    with open(filename, r) as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header row
        for line in f:
            rows[0] = parts[0].strip('"')
            rows[2] = int(parts[2])
            #print(parts)
            total += rows[2]*rows[3]
    #print('Total Cost', total)
    return total


import glob # grab files that match a specific pattern
files = glob.glob('data/portolio*.csv')
for filename in files:
    print(filename, porfoli_cost(file))



## Handling Bad Data and Exception Handling

some columns missing data value(None, N/A) => CAUSE calculation problems
use try block to catch

def porfoli_cost(filename):
    """
    total share of prices of a file
    """
    total = 0.0
    with open(filename, r) as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header row
        for line in f:
            try:
                rows[0] = parts[0].strip('"')
                rows[2] = int(parts[2])
            except ValueError as err: # store exception in error
                print("Bad Row", row)
                print("Reason", err) # print out error message to help debug
                continue # skip to next line
            total += rows[2]*rows[3]
    #print('Total Cost', total)
    return total




## Function Design Considerations

how to know catch ValueError Exception?  what errors are generated?
read documentation, see the exception, then add

ONE MISTAKE:
excetp Exception as err # this catches all exceptions, DANGEROUS practice
this will catch error that you are NOT expecting

            try:
                rows[0] = parts[0].strip('"')
                rows[2] = in(parts[2])
            except ValueError as err: # store exception in error
                print("Bad Row", row)
                print("Reason", err) # print out error message to help debug
                continue # skip to next line
            total += rows[2]*rows[3]

# if typo in rows[2], not int
will still run
BEST: try to narrow down to specific excetiopns.

BETTER PRACTICE: optional argument to silent warning, gives user to silent warning
def porfoli_cost(filename, errors='warn'): # by default, give warning, but gives option to silent warnings
    """
    total share of prices of a file
    """
    total = 0.0
    with open(filename, r) as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header row
        for line in f:
            try:
                rows[0] = parts[0].strip('"')
                rows[2] = int(parts[2])
            except ValueError as err: # store exception in error
                if errors == 'warn':
                    print("Bad Row", row)
                    print("Reason", err) # print out error message to help debug
                continue # skip to next line
            total += rows[2]*rows[3]
    #print('Total Cost', total)
    return total
total = porfoli_cost('a.csv', 'silent')# but silent arguemtn not CLEAR
#when have optional arguements, use keyword argument passing style
total = porfoli_cost('a.csv', errors='silent')# more readable, makes more sense

**** CAN FORCE people to use keyword argument passing!!!!!
Having a star * before the optional arguement
def porfoli_cost(filename, *,  errors='warn'): # if defined this way, HAVE TO use keyword passing


How to know the valid values for the optional arguments?
CHECK input

    # catch input
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of warn, silent, riase")


            except ValueError as err: # store exception in error
                if errors == 'warn':

                    print("Bad Row", row)
                    print("Reason", err) # print out error message to help debug
                elif errors = 'raise':
                    raise                # reraises the last exception
                else:
                    pass                # ignore
                continue # skip to next line







########---------5. Data Structure and Manipulation -------------############

builtin data types:


'''
LIKE RECORD, have different parts
tuples: immutable, heterogeneous types,  packing , unpacking
can do many operations like list, len(), index,
'''
t = ('A', '2015-32-0', 10, 4)# this is packing elements

# unpacking
name, data, shares, price = t


'''
list: mutable, homogenous(same) type, can modify, insert, len, change data,

'''



'''
set: {}, just keys, no values, no duplicates , eliminiate duplicates, membership testing using in
set(names) # eliminate duplicates
in operator : check memebership
'''
distinct_names = {'YHOO', 'IBM', 'AA'}



'''
dictionary: key-value mapping, has to have distinct keys, in operator

set value of centain key will REPLACE THE PREVIOUS value

also in operator

'''
prices = {'MSFT':23, 'YHOO': 34}


## can  combine different data types







########---------6.Library Functions and Impoprt-------------############

@import
import first loads the file and executes all the statements in the file in a ioslated
world. Have to use module name to get access to the model content
EX:
import math
math.cos(2)

@from math import sqrt #also loads the entire file, but only exposing the sqrt function


import is one-time operation, it caches all the modules imported!
will not load the module again if already loaded
the modules are stored in sys:
    import sys
    sys.modules['math'] # return where the module lives


find where the modules are?
import sys
sys.path


waht if do not want to print?
if __name__ == '__main__':
    print('Running')
    run()

python simple.py => will run and print out running
__name__ => '__main__'


if use "import simple", the print statement will not print
simple__name__ => simple



## Writing a general purpose CSV parsing module

row = ['AA', '2007-11-11', '100', '23.4']
types = [str, str, int, float]

for func, val in zip(types, row):
    print(func, val)

converted_row  = [func(val) for func, val in zip(types, row)]

MAKING A DICTIONARY

dict(zip(headers, converted))



## Making a package

how to organize large code moduels?
create a package, a directory that contains all .py files

touch __init__.py inside dir
portie dir(port.py, reader.py, __init__.py)

now can we import
import portie.reader # inside portie dir



PROBLEM:
from . import reader



__init__.py
# Purpose:
1. will execute when import any module, so we can perform initialization
steps of a package

2. lift symbols from submodules up a level
so that users do not need to know how you organize modules



########---------8. Inheritance -------------############

class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print("Parent Spam", self.value)

    def grok(self):
        print("Parent.grok")
        self.spam()


@1: add somthing to existing code
class Child1(Parent):

    def yow(self):
        print('Child1.yow')


c = Child1(32) # still need to pass a value, from parent
c.value  # 32
c.yow()


@2: redefine parent methods, override methods

class Child2(Parent):
    def spam(self):
        print("Child2.spam", self.value)

@3. wrap an existing method

class Child3(Parent):
    def spam(self):
        print("Child3.spam")
        super().spam()   # invoke the original spam in superclass


@4. add a new atribute

class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)    # initialize parent

c = Child4(42, 37)
c.value # 42
c.extra # 37


@5. Have more than one parent

class Parent2(object):
    def yow(self):
        print("Parent2.ywo")



class Child5(Parent, Parent2): # two parents will merge together, get all the combined functionalityies
    pass

c5 = Child5(32)
c5.grok()





## Inheritance in practice: building an extensible library







########---------9. Python Magic Methods -------------############

x = 10
x * 10 ==> x.__add__(10)
x / 10 = > x.__mul__(10)

names[0] ==> names.__getitem__(0)
names[1] ='FB' ==> names.__setitem__(1, 'FB')

# every operation has a dedicated speicial method to carry out the operation

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print('Add', other)

p = Point(2, 3)
p + 10
#Add 10
p + [1, 2, 3]
#Add [1, 2, 3]



## Making object printable and Debuggable

'''
__repr__(); # control the  representation of an object by defining __repr__
'''

h = Holding('AA', '2007-11-3', 1000, 32.2)
h
# Holding object at x9as9f
def __repr__(self):
    return "Holding({!r}, {!r}, {!r}, {!r})".format(self.name, self.name, self.share)
h
# HOlding('AA', '2007-11-3', 1000, 32.2)


'''
__str__(): create nice output string, used by print method
'''
def __str__():
    return "{} share of {} at {:0.2f}".format(self.name, self.share, self.price)

h = Holding('AA', '2007-11-3', 1000, 32.2)
print(h)
# 100 shares of AA at price




## Making a custom Container Object


def size(self):
    return len(self.holdings)
#BETTER
def __len__(self):
    return len(self.holdings)
len(HOLDING_INSTANCE)

def getHoldings(self, n):
    return self.holdings[n]
BETTER
def __getitem__(self, n):
    return self.holdings[n]

add some of the special methods to make a custom container, eaiser to work with
NOW you can len, [1] into the portofio like a builtin object, list



## Making a Custom Context Manager

#general pattern : open sth -> use it -> close it
#Possible to forget close

#make use of with
with open('portofio.csv') as f:
    data = f.read()

under the hood: __enter__() and __exit__()







###########--------------Encapsulation(owing the dot)-----------------##############





####------- Higher Order Functions and Closures ---------------#######


## Functions as objects

def greeting(name):
    print('Hello', name)

greeting('liu') # the function itself is an object, can pass it around, can store in varaibels
g = greeting
g("liu")
# you can append an object to a list, dictionary, pass around

#EX:
import time
def after(seconds, func):
    time.sleep(seconds)
    func()

def hello():
    print('hELLO')

after(5, hello)

names = ['dave', 'Thomas', "Lewis"]
names.sort(key=lambda x: name.upper())
a = lambda x: x*10
a(10) => 100



## Generating Code with Closures












def func(x, *args): # *args: any number of positional inputs
    print(x)
    print(args)

func(1, 2, 3, 4, 5)
#1
#(2, 3, 4, 5): the rest of the arguments collected into a tuple


def newFunc(x, **kwargs): # take any numer of keyword arguments
    print(x)
    print(kwargs)

newFunc(1, xmin=20, color='red')
#1
#{'xmin': 20, 'color': 'red'}: the kwargs will be placed into a dictionary

def both(*args, **kwargs): # takes any number of arguments, whatsoever
    print(args)
    print(kwargs)

both()
#()
#{}
both(1, 2, 3) #only have pisitional arguments
# (1, 2, 3)
#{}
both(1, 2, x=4, y=5)
#(1, 2)
#{'x': 4, 'y': 5}



###########----------------Decorators--------------------------##########

def add(x, y):
    print x + y
def sub(x, y):
    print x - y
def mul(x, y):
    return x * y

# add a log to every function
# to not repeat the same process.


def logged(func):
    # idea: add the logging around the function passed in
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

add = logged(add)
add(3, 4)
#('calling', 'add')
#7

sub = logged(sub)
sub(6, 4)
#('calling', 'sub')
#2

BY doint this, logging has been changing to one place

DECORATION: take an function, put a wrapper layer around it. It is like taking a
function and add some feature to it, decorate it.

so if we want to change the logging, we only need to change it in one place.

@logged
def mul(x, y):
    print x * y

mul(5, 3)
#('calling', 'mul')
#15


"""
NOTE: after doing this, orginal function will become wrapper objects, no proper
signatrue of the original functions
"""
from functools import wraps # use this @wraps in wrapper, this will copy the name,
#docstrings to the wrapper. THis is save orginal functions peroperies
def logged(func):
    # idea: add the logging around the function passed in
    @wraps
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

AFTER applying this @wrap decorator, the orginal functions have will their old
function name, docstrings. Less obvious that somebody applied a decorator to it

##Decorators with arguments(more advanced decorators)----
#what if want to change the format of the log message ?

#1. write an outer function that takes in the input(so input is avaible to rest of code)
from functools import wraps

def logformat(fmtStr):
    def logged(func):
        # idea: add the logging around the function passed in
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmtStr.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

@logformat("CALLING {func.__name__}")
def add(x, y):
    print x + y

add(4, 5)




#########-------------Class Decorators ---------###########

# apply decorators to class definitions

@logmethods
class Spam(object):
    def __init__(self, value):
        self.value = value

    def yow(self):
        print('yww')

    def grok(self):
        print('grok')


# put decorators logging to all the methods, could add @logged to each method

make a class decorator:

def logmethods(cls):
    for key, value in list(vars(cls).items()): # vars(Class) : list of everything defined in the class
        if callable(value):
            setattr(cls, key, logged(value))
    return cls




###### ------ Types and METACLSSES  Introduced ----###########

a = float()

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point(2, 5)
base = (object,) # one -tuple
print(type(p))

type is the class that creates other classes
we can customize type class through inheritance




##########Tracking subclasses in a framework

# supervises a collection of classes, classes inherits from metaclass
_formatters = {}
class TableMeta(type):
    def __init__(cls, clsname, bases, methods):
        super().__init__(clsname, bases, methods)
        if hasattr(cls, 'name'):
            _formatters[cls.name] = cls




# filling details in class defnitions
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

'''


##########-----------Iterators and generators---------------############

'''
names = ['Yahoo', 'IBM', 'AAPL']
for name in names:
    print(name)

Under the hood:

1). it = names.__iter__() # returns an iterator object
2). it.__next__() # 'Yahoo'
it.__next__() # 'IBM'
stops until stopIterationException

# using a generator

def countDown(n):
    print('count from', n)
    while n < 0:
        yield n  # emit a value
    print('Done')


#for x in countDown(5): # countDown function feeds values to the for loop
#    print(x)

c = countDown(5)
print(type(c)) #=> generator, suspend state, not going to run until you start iterate

it = c.__iter__()
it.__next__() # countDown in the suspend state, yield a number until call __next__ again



# CUSTOMIZE ITERATION

def grep(pattern, filename):
    with open(filename) as f :
        for line in f:
            if pattern in line:
                yield line
for line in grep('IBM', 'filepath'):
    print(line)

ANOTHER way to define generators:  similar to list comprehension: ()

nums = [1, 2, 3, 4, 5, 6]
squares = [x*x for x in nums]
squaresGenerator = (x*x for x in nums) #() gives an generator, do not generate the whole list
type(squaresGenerator) => generator
for x in squaresGenerator:
    print(x)


EX: sum((x*x for x in nums)) => can be simplified to sum(x*x for x in nums)
# this sums a generator without actually creating the temp list of nums
EX:
f = open('a.csv')
imb = (line for line in f if 'IBM' in line)
for line in imb:
    print(line)


NOTE: generators are one-time use, iterate once and then DONE!~
c =countDown(5)
for x in c:
    print(x)
# only work once, will NOT run if for x in c again!

If want to iterate multiple times, create an class to do that
class CountDown(object):
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
# now we can call c = Countdown(5) multiples times


#####watching a real-time data source with a Generator, ex log file on a server

tail -f PATH-TO-LOG-FILE

# write python file that watches this log file

import os
import time
f = open('a.csv', 'r')
f.seek(0, os.SEEK_END) # go to the end of the file

while True:
    line = f.readline()
    if not line:
        time.sleep(0.1)
        continue  # retry
    #print('Got line:', line)
    row = line.split(',')
    change = float(row[4])
    if change < 0:
        name = row[0]
        price = row[1]
        print('{:>10s} {:>10s} {:>10.2f}'.format(name, price, change)) # print a table

EX: use generators
def follow(filename): # sits there constantly monitoring the file , extremely general, just reading lines, not related to content

    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue  # retry
        yield line

for line in follow('a.csv'):
    row = line.split(',')
    change = float(row[4])
    if change < 0:
        name = row[0]
        price = row[1]
        print('{:>10s} {:>10s} {:>10.2f}'.format(name, price, change))



####### Processing Pipelines and Workflows

tail -f a.csv | egrep "IBM|MSFT|CAT|AA" => only find the selected lines

lines = follow('b.csv')
lines.__next__()

# we can take this data and feed into other functions with a for loop
rows = csv.reader(lines)
rows.__next__() = > ['', '', ....]
